from django.shortcuts import render
from django.http import HttpResponde
from django.contrib import messages
from . import models
from . import forms
# Create your views here.



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