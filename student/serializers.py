from rest_framework import serializers
from django.contrib.auth.models import User

# from rest_framework import serializers
from .models import Student_T

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_T
        fields = '__all__'  # Include all fields
       