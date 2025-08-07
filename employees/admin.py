from django.contrib import admin
from .models import Department, Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'date_joined')
    list_filter = ('department', 'date_joined')
    search_fields = ('name', 'email', 'department__name')
    date_hierarchy = 'date_joined'
    ordering = ('-date_joined',)
