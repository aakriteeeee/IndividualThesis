# healthtracker/apps.py

from django.apps import AppConfig

class HealthTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'healthtracker'

    def ready(self):
        # Import and initialize any signals or tasks related to your app
        from . import signals
