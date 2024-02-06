# healthtracker/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UserProfile, HealthData, Specialty, Doctor, Appointment, Blog

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('date_of_birth', 'bio', 'profile_picture')

class HealthDataForm(forms.ModelForm):
    class Meta:
        model = HealthData
        fields = ['date', 'weight', 'height', 'blood_pressure', 'heart_rate']
        # Add more fields as needed for your health data       

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['specialty', 'availability']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'appointment_date', 'reason']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
