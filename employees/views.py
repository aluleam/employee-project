from rest_framework import viewsets, filters
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer
from django_filters.rest_framework import DjangoFilterBackend

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['department', 'date_joined']
    search_fields = ['name', 'email']
    ordering_fields = ['date_joined', 'name']
    ordering = ['-date_joined']