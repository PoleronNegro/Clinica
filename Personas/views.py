from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Detalle.models import Genero
# Create your views here.
<<<<<<< HEAD



def medico(request):
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
    return render(request,'personas/base.html/vista_medico/.html',context)
=======
#Traer genero
def traerGenero():
    generos = Genero.objects.all()
    return generos
    
#modificado por oscar
def inicio(request):
    return render(request,'personas/inicio.html')
#modificado por oscar
def personas(request):
    context = {
        'genero':traerGenero()
    }
    return render(request,'personas/Vista_Paciente/vista_pacientes.html',context) 
#modificado por oscar
def login(request):
    return render(request,'personas/Login/vista_login.html')
#modificado por oscar
def vista_medico(request):
    return render(request,'personas/Vista_Medico/vista_medicos.html')
>>>>>>> 7f5b20bf290e7a1062275089554f48bd2b7e3132
