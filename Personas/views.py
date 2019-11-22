from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from . import models
from . import forms
# Create your views here.

#modificado por oscar
def inicio(request):
    return render(request,'Personas/templates/Personas/vistas_login.html')

#modificado por oscar
def medico(request):
    return render(request,'Personas/medico.html')
  
form = Medicoforms()
    if request.method == 'POST':
        nuevo = Medicoforms(request.POST)
        if nuevo.is_valid():
            nuevo.save()
            messages.SUCCES(request,'doctor guardado')
            redirect('inicio')


#vistas administrativo creado por osvaldo 

def registrohora(request):
    return HttpResponse ('Registro de hora')


def modificardatospaciente(request, rut_paciente):
    return HttpResponse ('Modificar datos paciente')
    
def mostrarhora (request):
    return HttpResponse ('Mostrar horas')