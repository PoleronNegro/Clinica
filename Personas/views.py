from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

#modificado por oscar
def inicio(request):
    return render(request,'personas/inicio.html')
#modificado por oscar
def personas(request):
    return render(request,'personas/Vista_Paciente/vista_pacientes.html') 
#modificado por oscar
def login(request):
    return render(request,'personas/Login/vista_login.html')
#modificado por oscar
def vista_medico(request):
    return render(request,'personas/Vista_Medico/vista_medicos.html')
