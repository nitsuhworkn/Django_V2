from django.contrib.auth.models import User  # for API
from django.db import models

# Create your models here.
class Student_T(models.Model):
    student_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.student_name