# employee_project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from employees import views as emp_views
from attendance import views as att_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'departments', emp_views.DepartmentViewSet)
router.register(r'employees', emp_views.EmployeeViewSet)
router.register(r'attendance', att_views.AttendanceViewSet)
router.register(r'performance', att_views.PerformanceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    # Add these token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]