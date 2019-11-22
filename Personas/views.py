from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def inicio(request):
    return render(request,'Personas/templates/Personas/vistas_login.html')

def medico(request):
    return render(request,'Personas/medico.html')

    