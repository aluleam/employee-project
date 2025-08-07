from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Attendance, Performance
from .serializers import AttendanceSerializer, PerformanceSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        'employee': ['exact'],
        'employee__department': ['exact'],  # filter by department
        'employee__date_joined': ['exact', 'gte', 'lte'],  # filter by date_joined with ranges
        'date': ['exact', 'gte', 'lte'],   # filter by attendance date
        'status': ['exact'],
    }
    ordering_fields = ['date', 'employee__name', 'employee__department']

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        'employee': ['exact'],
        'employee__department': ['exact'],
        'employee__date_joined': ['exact', 'gte', 'lte'],
        'rating': ['exact', 'gte', 'lte'],
        'review_date': ['exact', 'gte', 'lte'],
    }
    ordering_fields = ['rating', 'review_date', 'employee__name', 'employee__department']
