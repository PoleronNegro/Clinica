from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

#modificado por oscar
def login(request):
    return render(request,'personas/Login/vista_login.html')
