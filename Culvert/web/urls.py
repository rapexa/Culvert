from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('auth/register', views.register, name='register'),
    path('auth/login', views.login, name='login'),
    path('auth/whoami', views.whoami, name='whoami'),
    path('app/calculate', views.Calculate, name='Calculate'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]