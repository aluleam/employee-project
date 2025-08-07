from django.http import HttpResponse
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from employees import views as emp_views
from attendance import views as att_views

router = routers.DefaultRouter()
router.register(r'departments', emp_views.DepartmentViewSet)
router.register(r'employees', emp_views.EmployeeViewSet)
router.register(r'attendance', att_views.AttendanceViewSet)
router.register(r'performance', att_views.PerformanceViewSet)

def home(request):
    return HttpResponse("<h1>Welcome to Employee Management API</h1>")

urlpatterns = [
    path('', home),  # root URL
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
