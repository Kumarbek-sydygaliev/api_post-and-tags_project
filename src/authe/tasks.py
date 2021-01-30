from __future__ import absolute_import, unicode_literals
from api_example.celery import app
from django.core.mail import send_mail
from django.conf import settings

@app.task()
def add(x, y):
    print(x + y)
    return x + y

@app.task()
def send_verified_link(message, email):
    send_mail('Blog', message, settings.DEFAULT_EMAIL_FROM, [email,])

@app.task()
def send_password_reset_link(message, email):
    send_mail('Blog', message, settings.DEFAULT_EMAIL_FROM, [email,])