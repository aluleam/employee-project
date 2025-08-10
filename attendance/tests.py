from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from employees.models import Department, Employee
from attendance.models import Attendance, Performance 
from rest_framework_simplejwt.tokens import RefreshToken
import datetime

class AttendanceModelTest(TestCase):
    def setUp(self):
        self.dept = Department.objects.create(name="Sales")
        self.emp = Employee.objects.create(
            name="Tom",
            email="tom@example.com",
            phone="1112223333",
            address="10 Downing St",
            date_joined=datetime.date(2022, 12, 1),
            department=self.dept
        )
        self.att = Attendance.objects.create(
            employee=self.emp,
            date=datetime.date(2023, 7, 15),
            status='P'
        )

    def test_str(self):
        self.assertEqual(str(self.att.employee), "Tom")  # You can customize __str__ in Attendance if you want

class PerformanceModelTest(TestCase):
    def setUp(self):
        self.dept = Department.objects.create(name="Sales")
        self.emp = Employee.objects.create(
            name="Jerry",
            email="jerry@example.com",
            phone="4445556666",
            address="123 Some St",
            date_joined=datetime.date(2023, 1, 1),
            department=self.dept
        )
        self.perf = Performance.objects.create(
            employee=self.emp,
            rating=4,
            review_date=datetime.date(2023, 7, 10)
        )

    def test_str(self):
        self.assertEqual(str(self.perf), "Jerry - 4")

class AttendanceAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass123')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        
        self.client = APIClient()
        
        self.dept = Department.objects.create(name="Marketing")
        self.emp = Employee.objects.create(
            name="Anna",
            email="anna@example.com",
            phone="7778889999",
            address="456 Maple St",
            date_joined=datetime.date(2023, 2, 1),
            department=self.dept
        )
        
        self.att_url = reverse('attendance-list')  # Adjust name if different
        self.att_detail_url = lambda pk: reverse('attendance-detail', args=[pk])

    def test_auth_required(self):
        res = self.client.get(self.att_url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_create_attendance(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        data = {
            "employee": self.emp.id,
            "date": "2023-08-01",
            "status": "P"
        }
        res = self.client.post(self.att_url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['status'], "P")
    
    def test_get_attendance_list(self):
        Attendance.objects.create(employee=self.emp, date=datetime.date(2023, 8, 1), status='A')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        res = self.client.get(self.att_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(len(res.data['results']) >= 1)

    def test_get_attendance_detail(self):
        att = Attendance.objects.create(employee=self.emp, date=datetime.date(2023, 8, 1), status='L')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        res = self.client.get(self.att_detail_url(att.id))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['status'], 'L')

class PerformanceAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass123')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        
        self.client = APIClient()
        
        self.dept = Department.objects.create(name="Finance")
        self.emp = Employee.objects.create(
            name="Sam",
            email="sam@example.com",
            phone="2223334444",
            address="789 Oak St",
            date_joined=datetime.date(2023, 3, 1),
            department=self.dept
        )
        
        self.perf_url = reverse('performance-list')  # Adjust name if different
        self.perf_detail_url = lambda pk: reverse('performance-detail', args=[pk])

    def test_auth_required(self):
        res = self.client.get(self.perf_url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_performance(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        data = {
            "employee": self.emp.id,
            "rating": 5,
            "review_date": "2023-08-01"
        }
        res = self.client.post(self.perf_url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['rating'], 5)

    def test_get_performance_list(self):
        Performance.objects.create(employee=self.emp, rating=3, review_date=datetime.date(2023, 8, 1))
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        res = self.client.get(self.perf_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(len(res.data['results']) >= 1)

    def test_get_performance_detail(self):
        perf = Performance.objects.create(employee=self.emp, rating=2, review_date=datetime.date(2023, 8, 2))
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        res = self.client.get(self.perf_detail_url(perf.id))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['rating'], 2)
