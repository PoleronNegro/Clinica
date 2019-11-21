from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('acounts/', include('django.contrib.auth.ulrs')),
]