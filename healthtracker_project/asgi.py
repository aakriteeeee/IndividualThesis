# """
# ASGI config for healthtracker_project project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
# """

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "healthtracker_project.settings")

# django_asgi_application = get_asgi_application()

# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# import healthtracker.routing

# application = ProtocolTypeRouter({
#     "http": django_asgi_application,
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             healthtracker.routing.websocket_urlpatterns
#         )
#     ),
# })

"""
ASGI config for healthtracker_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "healthtracker_project.settings")

application = get_asgi_application()

