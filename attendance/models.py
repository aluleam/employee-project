from django.db import models
from employees.models import Employee

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('employee', 'date')

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performance')
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    review_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.rating}"