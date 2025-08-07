from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet, PerformanceViewSet

router = DefaultRouter()
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance', PerformanceViewSet)

urlpatterns = router.urls
