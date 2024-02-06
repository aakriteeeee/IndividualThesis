# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import UserProfile, HealthData, Doctor, Specialty, Appointment, Blog
from .personalization import train_personalization_model, get_personalized_recommendations
from datetime import datetime

class UserProfileModelTest(TestCase):
    def test_user_profile_creation(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        profile = UserProfile.objects.create(user=user, date_of_birth=datetime(1990, 1, 1))
        self.assertEqual(profile.user.username, 'testuser')

class HealthDataModelTest(TestCase):
    def test_health_data_creation(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        health_data = HealthData.objects.create(user=user, date=datetime.now(), weight=70.5, height=175, blood_pressure='120/80', heart_rate=70)
        self.assertEqual(health_data.user.username, 'testuser')

class DoctorModelTest(TestCase):
    def test_doctor_creation(self):
        specialty = Specialty.objects.create(name='Cardiologist')
        doctor = Doctor.objects.create(name='Dr. Smith', specialty=specialty, availability='Monday - Friday')
        self.assertEqual(doctor.name, 'Dr. Smith')

class AppointmentModelTest(TestCase):
    def test_appointment_creation(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        specialty = Specialty.objects.create(name='Cardiologist')
        doctor = Doctor.objects.create(name='Dr. Smith', specialty=specialty, availability='Monday - Friday')
        appointment = Appointment.objects.create(user=user, doctor=doctor, appointment_date=datetime.now(), reason='Regular checkup')
        self.assertEqual(appointment.user.username, 'testuser')

class BlogModelTest(TestCase):
    def test_blog_creation(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        blog = Blog.objects.create(title='Healthcare Blog', content='This is a blog post about healthcare.', author=user)
        self.assertEqual(blog.title, 'Healthcare Blog')

class PersonalizationTest(TestCase):
    def test_personalization_model(self):
        # Test training the personalization model
        clf = train_personalization_model()
        self.assertIsNotNone(clf)

    def test_personalized_recommendation(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        user_profile = UserProfile.objects.create(user=user, date_of_birth=datetime(1990, 1, 1))
        recommendation = get_personalized_recommendations(user)
        self.assertTrue(recommendation.startswith('Your personalized recommendation'))

