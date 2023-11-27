from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('auth/register', views.register, name='register'),
    path('auth/login', views.login, name='login'),
    path('auth/whoami', views.whoami, name='whoami'),
]