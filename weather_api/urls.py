from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.WeatherAPIView.as_view(), name='home'),
]