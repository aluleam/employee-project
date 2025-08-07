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
        # Create departments if they don't exist
        departments = ['HR', 'Engineering', 'Marketing', 'Sales', 'Finance']
        dept_objs = []
        for name in departments:
            dept_obj, created = Department.objects.get_or_create(name=name)
            dept_objs.append(dept_obj)

        # Create employees
        employees = []
        for _ in range(50):
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                address=fake.address(),
                date_joined=fake.date_between(start_date='-5y', end_date='today'),
                department=random.choice(dept_objs)
            )
            employees.append(emp)

        # Create attendance records for last 30 days per employee
        for emp in employees:
            for day in range(30):
                Attendance.objects.create(
                    employee=emp,
                    date=datetime.now().date() - timedelta(days=day),
                    status=random.choice(['P', 'A', 'L'])  # Use correct status codes your model expects
                )

        # Create performance reviews for last 12 months per employee
        for emp in employees:
            for month_offset in range(12):
                review_date = datetime.now().date() - timedelta(days=month_offset * 30)
                if review_date >= emp.date_joined:
                    Performance.objects.create(
                        employee=emp,
                        rating=random.randint(1, 5),
                        review_date=review_date
                    )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))