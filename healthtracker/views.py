
from .models import Specialty, Doctor, HealthData, Appointment, Blog
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from healthtracker.forms import SignUpForm , UserProfileForm , HealthDataForm, DoctorForm, AppointmentForm, BlogForm# Updated import statement
from .personalization import get_personalized_recommendations
def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with your actual home page URL
    else:
        user_form = SignUpForm()
        profile_form = UserProfileForm()
    return render(request, 'healthtracker/signup.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def track_health_data(request):
    if request.method == 'POST':
        form = HealthDataForm(request.POST)
        if form.is_valid():
            health_data = form.save(commit=False)
            health_data.user = request.user
            health_data.save()
            return redirect('health_data_list')  # Redirect to health data list page
    else:
        form = HealthDataForm()
    return render(request, 'healthtracker/track_health_data.html', {'form': form})

@login_required
def health_data_list(request):
    health_data_entries = HealthData.objects.filter(user=request.user)
    return render(request, 'healthtracker/health_data_list.html', {'health_data_entries': health_data_entries})


def home(request):
    user = request.user
    if user.is_authenticated:
        recommendations = get_personalized_recommendations(user)
        return render(request, 'healthtracker/home.html', {'recommendations': recommendations})
    else:
        return render(request, 'healthtracker/home.html')




def doctors_list(request):
    specialties = Specialty.objects.all()
    doctors = Doctor.objects.all()

    return render(request, 'healthtracker/doctors_list.html', {'specialties': specialties, 'doctors': doctors})



@login_required
def register_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.user = request.user
            doctor.save()
            return redirect('home')  # Replace 'home' with your actual home page URL
    else:
        form = DoctorForm()
    return render(request, 'healthtracker/register_doctor.html', {'form': form})



@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointment_list')  # Redirect to appointment list page
    else:
        form = AppointmentForm()
    return render(request, 'healthtracker/book_appointment.html', {'form': form})

@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'healthtracker/appointment_list.html', {'appointments': appointments})



@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_list')  # Redirect to blog list page
    else:
        form = BlogForm()
    return render(request, 'healthtracker/create_blog.html', {'form': form})

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'healthtracker/blog_list.html', {'blogs': blogs})
