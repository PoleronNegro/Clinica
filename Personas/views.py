from django.shortcuts import render
from django.http import HttpResponde
from django.contrib import messages
from . import models
from . import forms
# Create your views here.



def medico(request):
    form = Medicoforms()
    if request.method == 'POST':
        nuevo = Medicoforms(request.POST)
        if nuevo.is_valid():
            nuevo.save()
            messages.SUCCES(request,'doctor guardado')
            redirect('inicio')