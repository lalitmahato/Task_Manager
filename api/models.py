from django.contrib.auth.models import User
from django.db import models
from datetime import date

# Create your models here.
gender_choice = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

role_choice = (
    ('Supervisor','Supervisor'),
    ('Intern','Intern'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, null=True)
    first_name = models.CharField(max_length=500, null=True)
    last_name = models.CharField(max_length=500, null=True)
    email = models.EmailField(max_length=500, null=True)
    phone_no = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True, choices=gender_choice)
    date_of_birth = models.DateField(null=True)
    role = models.CharField(max_length=100, default='Intern', blank=True, null=True, choices=role_choice)

    def __str__(self):
        return self.user.username

class Task(models.Model):
    assigned = models.ForeignKey(UserProfile, on_delete= models.CASCADE)
    title = models.CharField(max_length=500, null=True)
    task_description = models.CharField(max_length=1000, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title

class Attendance(models.Model):
    username = models.ForeignKey(UserProfile, on_delete= models.CASCADE, null=True)
    date = models.DateField(default=date.today, null=True)
    attendence_status = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.username.user.username
