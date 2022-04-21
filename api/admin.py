from django.contrib import admin
from .models import UserProfile, Task, Attendance
# Register your models here.

@admin.register(UserProfile)
class User_Profile(admin.ModelAdmin):
    list_display = ['user','first_name','last_name','email','phone_no','role']

@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ['assigned', 'title','task_description','completed']

@admin.register(Attendance)
class Attendance(admin.ModelAdmin):
    list_display = ['username', 'date','attendence_status']