from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Detalle.models import Genero
# Create your views here.

#sebastian
def vista_medico(request):
    form = Doctor()
    if request.method == 'POST':
        newForm = Doctor(request.POST)
        if newForm.is_valid():
            newForm.save()
            messages.SUCCESS(request,'Datos Guardados con exito')
            redirect('inicio')
        else:
            form = newForm    
    context = {
        'form':form
    }
    return render(request,'personas/Vista_Medico/vista_medico.html',context)

#hecho por sebastians alexis 
def  vista_administracion(request):
    forms = Paciente()
    if request.method == 'POST':
        newForm = Paciente(request.POST)
        if newForm.is_valid():
            newForm.save()
            messages.SUCCESS(request,'')
            redirect('inicio')
        else:
            form = newForm    
    context = {
        'form':forms
    }
    return render(request,'personas/Vista_Administrativa/vista_administracion.html',context)   

#hecho por sebastian
def Adm(request):
    Datosdoctor =Doctor.objects.all()
    return Datosdoctor
   

#Traer genero
def traerGenero():
    generos = Genero.objects.all()
    return generos

#modificado por oscar
def inicio(request):
    return render(request,'personas/home.html')

#modificado por oscar
def personas(request):
    context = {
        'genero':traerGenero()
    }
    return render(request,'personas/Vista_Paciente/vista_pacientes.html',context) 
    
#modificado por oscar
def login(request):
    return render(request,'personas/Login/vista_login.html')

#creado por osvaldo 
def informehoras(request):
    context = {'fecha_hora'}