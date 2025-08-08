from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from employees import views as emp_views
from attendance import views as att_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()
router.register(r'departments', emp_views.DepartmentViewSet)
router.register(r'employees', emp_views.EmployeeViewSet)
router.register(r'attendance', att_views.AttendanceViewSet)
router.register(r'performance', att_views.PerformanceViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Employee Management API",
        default_version='v1',
        description="API documentation for the Employee Management System",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('employees.urls')),
    path('accounts/', include('employees.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('charts/', emp_views.chart_page, name='charts'),

    path('swagger/', login_required(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),
    path('redoc/', login_required(schema_view.with_ui('redoc', cache_timeout=0)), name='schema-redoc'),

    path('', RedirectView.as_view(url='/swagger/', permanent=False)),
]
