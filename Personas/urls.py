from django.urls import path,include
from . import views

app_name = 'personas'

urlpatterns = [
    #modificado por oscar
    path('inicio/', views.inicio,name='inicio'),
    path('vista_login/', views.login,name='login'),
    path('vista_pacientes/', views.personas,name='vista_pacientes'),
    path('vista_medicos/', views.vista_medico,name='vista_medico'),
    path('vista_adm/',views.vista_adm,name='vista_adms'),
]
