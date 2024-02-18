"""
WSGI config for vercel_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vercel_app.settings")
if os.environ.get("ENV") == "production":
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

app = get_wsgi_application()
