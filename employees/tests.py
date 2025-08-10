from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from employees.models import Department, Employee
from rest_framework_simplejwt.tokens import RefreshToken
import datetime

class DeptModelTest(TestCase):
    def setUp(self):
        self.dept = Department.objects.create(name="Engineering")

    def test_str(self):
        self.assertEqual(str(self.dept), "Engineering")

class EmpModelTest(TestCase):
    def setUp(self):
        self.dept = Department.objects.create(name="Engineering")
        self.emp = Employee.objects.create(
            name="John Doe",
            email="john@example.com",
            phone="1234567890",
            address="123 Main St",
            date_joined=datetime.date(2023, 1, 1),
            department=self.dept
        )

    def test_str(self):
        self.assertEqual(str(self.emp), "John Doe")

class EmpAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        self.client = APIClient()
        
        self.dept = Department.objects.create(name="HR")
        
        self.emp = Employee.objects.create(
            name="Jane Smith",
            email="jane@example.com",
            phone="0987654321",
            address="456 Elm St",
            date_joined=datetime.date(2023, 5, 15),
            department=self.dept
        )

        self.emp_url = reverse('employee-list')
        self.dept_url = reverse('department-list')

    # Dept API
    def test_dept_auth(self):
        res = self.client.get(self.dept_url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(res.data['detail'], "Authentication credentials were not provided.")

    def test_dept_list(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        res = self.client.get(self.dept_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(any(d['name'] == "HR" for d in res.data['results']))

    def test_dept_create(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        res = self.client.post(self.dept_url, {"name": "Finance"}, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['name'], "Finance")

    # Employee API
    def test_emp_auth(self):
        res = self.client.get(self.emp_url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(res.data['detail'], "Authentication credentials were not provided.")

    def test_emp_list(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        res = self.client.get(self.emp_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['results']), 1)
        self.assertEqual(res.data['results'][0]['name'], 'Jane Smith')

    def test_emp_create(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        data = {
            "name": "Alice Johnson",
            "email": "alice@example.com",
            "phone": "5555555555",
            "address": "789 Pine St",
            "date_joined": "2024-03-10",
            "department": self.dept.id
        }
        res = self.client.post(self.emp_url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['name'], "Alice Johnson")

    def test_emp_get(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        url = reverse('employee-detail', args=[self.emp.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['email'], self.emp.email)

    def test_emp_update(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        url = reverse('employee-detail', args=[self.emp.id])
        data = {
            "name": "Jane Updated",
            "email": self.emp.email,
            "phone": self.emp.phone,
            "address": self.emp.address,
            "date_joined": str(self.emp.date_joined),
            "department": self.dept.id
        }
        res = self.client.put(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['name'], "Jane Updated")

    def test_emp_patch(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        url = reverse('employee-detail', args=[self.emp.id])
        res = self.client.patch(url, {"address": "New Address 123"}, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['address'], "New Address 123")

    def test_emp_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        url = reverse('employee-detail', args=[self.emp.id])
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)