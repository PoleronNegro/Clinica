from django.contrib import admin
from django.urls import path,include
from Personas import views

urlpatterns = [
    #modificado por oscar
    path('/vista_login',views.inicio,name='inicio'),
]
