from django.test import TestCase
from .models import Department, Employee
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class EmployeeModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="Engineering")
        self.employee = Employee.objects.create(
            name="John Doe",
            email="john@example.com",
            phone_number="1234567890",
            address="123 Main St",
            date_of_joining="2023-01-01",
            department=self.department
        )

    def test_employee_str(self):
        self.assertEqual(str(self.employee), "John Doe")

class EmployeeAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.department = Department.objects.create(name="HR")
        self.employee = Employee.objects.create(
            name="Jane Smith",
            email="jane@example.com",
            phone_number="0987654321",
            address="456 Elm St",
            date_of_joining="2023-05-15",
            department=self.department
        )

    def test_get_employees(self):
        url = reverse('employee-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Jane Smith')