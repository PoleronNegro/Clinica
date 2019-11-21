from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('aacounts/', include('django.contrib.auth.ulrs')),
]