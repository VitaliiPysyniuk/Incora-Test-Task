"""
WSGI config for incora_test_task project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from socketio import WSGIApp, Server

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itt_core.settings')

sio = Server()
application = WSGIApp(sio, get_wsgi_application())
