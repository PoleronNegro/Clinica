from django.urls import path,include
from . import views

app_name = 'personas'

urlpatterns = [
    #modificado por oscar
    path('inicio/', views.inicio,name='inicio'),
    path('vista_login/', views.login,name='login'),
    path('vista_pacientes/', views.personas,name='vista_pacientes'),
    path('vista_medico/', views.vista_medico,name='vista_medico'),
    path('vista_administracion/',views.vista_administracion,name='vista_administracion'),
]
