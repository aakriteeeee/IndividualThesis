"""
URL configuration for healthtracker_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from healthtracker import views
from healthtracker.views import signup, track_health_data, health_data_list, doctors_list, home
urlpatterns = [
    path("admin/", admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('health/', include('healthtracker.urls')),  # Assuming health data tracking URLs are defined in healthtracker app
    path('doctors/', views.doctors_list, name='doctors_list'),
    path('appointment/', views.book_appointment, name='book_appointment'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('', views.home, name='home'),

]



    # # path("admin/", admin.site.urls), 
    # # path('signup/', signup, name='signup'),
    # path('health/', include('healthtracker.urls')),
    # path('list/', health_data_list, name='health_data_list'),
    # path('doctors/', doctors_list, name='doctors_list'),
    # path('', home, name='home'),






