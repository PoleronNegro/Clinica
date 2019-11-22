from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('acounts/', include('django.contrib.auth.ulrs')),
    path('medico/',views.medico,name='inicio'),
    #paths creados por osvaldo
    path('mostrarhora/',views.mostrarhora, name='mostrar hora'),
    path('registrohora/',views.registrohora,name='registrar hora')
]