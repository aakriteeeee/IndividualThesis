from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Add additional fields as needed for the user profile
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)


    def __str__(self):
        return self.username
    
class HealthData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()
    height = models.FloatField()
    blood_pressure = models.CharField(max_length=10)
    heart_rate = models.IntegerField()
    # Add more fields as needed for your health data

    def __str__(self):
        return f"{self.user.username}'s Health Data on {self.date}"    
    



class Specialty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    availability = models.CharField(max_length=200)

    def __str__(self):
        return self.name




class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  # Assuming you have a Doctor model
    appointment_date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.doctor.name} - {self.appointment_date}'


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
