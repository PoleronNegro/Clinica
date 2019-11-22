from django.contrib import admin
from django.urls import path,include
from Personas import views

urlpatterns = [
    path('vista_login/',views.medico,name='Login'),
    #path('vista_medicos/',views.medico,name='medico'),
]