from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('employees-per-department/', views.employees_per_department, name='employees-per-department'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('charts/', views.chart_page, name='chart-page'),
]
