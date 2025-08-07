from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Attendance, Performance
from .serializers import AttendanceSerializer, PerformanceSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['employee', 'date', 'status']
    search_fields = ['employee__name']
    ordering_fields = ['date']
    ordering = ['-date']
    permission_classes = [IsAuthenticated]

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['employee', 'review_date', 'rating']
    search_fields = ['employee__name']
    ordering_fields = ['review_date', 'rating']
    ordering = ['-review_date']
    permission_classes = [IsAuthenticated]
