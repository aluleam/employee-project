from django.core.management.base import BaseCommand
from employees.models import Department, Employee
from attendance.models import Attendance, Performance
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

class Command(BaseCommand):
    help = 'Seeds the database with sample data'

    def handle(self, *args, **options):
        # Create departments
        departments = ['HR', 'Engineering', 'Marketing', 'Sales', 'Finance']
        dept_objs = [Department.objects.create(name=name) for name in departments]
        
        # Create employees
        employees = []
        for _ in range(50):
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.address(),
                date_joined=fake.date_between(start_date='-5y', end_date='today'),
                department=random.choice(dept_objs)
            )
            employees.append(emp)
        
        # Create attendance records
        for emp in employees:
            for day in range(30):  # 30 days of records
                Attendance.objects.create(
                    employee=emp,
                    date=datetime.now() - timedelta(days=day),
                    status=random.choice(['P', 'A', 'L'])
                )
        
        # Create performance reviews
        for emp in employees:
            Performance.objects.create(
                employee=emp,
                rating=random.randint(1, 5),
                review_date=fake.date_between(start_date=emp.date_joined, end_date='today')
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))