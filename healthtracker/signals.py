# healthtracker/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create a user profile when a new user is registered.
    """
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=get_user_model())
def save_user_profile(sender, instance, **kwargs):
    """
    Signal to save the user profile whenever the user is saved.
    """
    try:
        instance.profile.save()
    except UserProfile.DoesNotExist:
        # Handle the case where the user profile does not exist
        pass
