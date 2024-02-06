from django.contrib import admin

# Register your models here.

# healthtracker/admin.py

from django.contrib import admin
from .models import Specialty, Doctor

class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'is_available')

admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Doctor, DoctorAdmin)

