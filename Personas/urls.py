from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('acounts/', include('django.contrib.auth.ulrs')),
    path('medico/',views.medico,name='inicio')
]