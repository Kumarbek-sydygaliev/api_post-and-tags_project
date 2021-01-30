from django.urls import path
from .views import registration, confirm, login, reset_password, confirm_password

urlpatterns = [
    path('registration/', registration, name = 'registration'),
    path('login/', login, name = 'login'),
    path('reset/password/', reset_password, name = 'reset_password'),
    path('confirm/password/<str:code>/', confirm_password, name = 'confirm_password'),
    path('<str:code>/', confirm, name = 'register'),
]
