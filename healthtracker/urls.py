# healthtracker/urls.py

from django.urls import path
from .views import (signup,
                    track_health_data, 
                    health_data_list,
                    doctors_list,
                    register_doctor,
                    home,book_appointment, 
                    appointment_list, 
                    create_blog, 
                    blog_list,
)
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('track/', track_health_data, name='track_health_data'),
    path('list/', health_data_list, name='health_data_list'),
    path('doctors/', doctors_list, name='doctors_list'),
    path('register_doctor/', register_doctor, name='register_doctor'),
    path('', home, name='home'),
    path('book_appointment/', book_appointment, name='book_appointment'),
    path('appointment_list/', appointment_list, name='appointment_list'),
    path('create_blog/', create_blog, name='create_blog'),
    path('blog_list/', blog_list, name='blog_list'),
    # Add more URLs as needed
   


]
