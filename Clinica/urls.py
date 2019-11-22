"""Clinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Personas.urls import path,include 
from Personas import views as vistasPersonas

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('',include('personas.urls'))
=======
    path('', vistasPersonas.inicio,name='inicio'),
    path('login/', vistasPersonas.login,name='vista_login'),
    path('vista_pacientes/', vistasPersonas.personas,name='vista_pacientes'),
    path('vista_medico/', vistasPersonas.vista_medico,name='vista_medico'),
>>>>>>> 7f5b20bf290e7a1062275089554f48bd2b7e3132
]
