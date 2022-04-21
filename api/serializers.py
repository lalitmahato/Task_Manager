from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserProfile, Task, Attendance

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],validated_data['email'], validated_data['password'])
        return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']



# Profile Serializer
class UserProfileSerializerSupervisor(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name','email', 'phone_no','gender','date_of_birth','role']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name','email', 'phone_no','gender','date_of_birth']

class UserProfileSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


# Task Serializer
class TaskSerializerSupervisor(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['assigned','title','task_description','completed']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
class TaskSerializerIntern(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['completed']

# Attendance
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class MakeAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['date','attendence_status']