from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from employees.models import Department, Employee
from attendance.models import Attendance
from rest_framework_simplejwt.tokens import RefreshToken
import datetime

class AttendanceAPITest(TestCase):
    def setUp(self):
        # Create user and JWT token
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        self.client = APIClient()

        # Setup department and employee
        self.department = Department.objects.create(name="Engineering")
        self.employee = Employee.objects.create(
            name="John Doe",
            email="john@example.com",
            phone="1234567890",
            address="123 Main St",
            date_joined=datetime.date(2023, 1, 1),
            department=self.department
        )
        
        # Create an attendance record
        self.attendance = Attendance.objects.create(
            employee=self.employee,
            date=datetime.date(2025, 8, 9),
            status='P'
        )

        self.list_url = reverse('attendance-list')  # Adjust if your router basename is different

    def test_authentication_required(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], "Authentication credentials were not provided.")

    def test_get_attendance_list(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['status'], 'P')

    def test_create_attendance(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        data = {
            "employee": self.employee.id,
            "date": "2025-08-10",
            "status": "A"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'A')

    def test_get_attendance_detail(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        url = reverse('attendance-detail', args=[self.attendance.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'P')

    def test_update_attendance(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        url = reverse('attendance-detail', args=[self.attendance.id])
        data = {
            "employee": self.employee.id,
            "date": str(self.attendance.date),
            "status": "L"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'L')

    def test_partial_update_attendance(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        url = reverse('attendance-detail', args=[self.attendance.id])
        data = {"status": "A"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'A')

    def test_delete_attendance(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        url = reverse('attendance-detail', args=[self.attendance.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)