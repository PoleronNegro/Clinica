from django.urls import path,include
from . import views

app_name = 'personas'

urlpatterns = [
    #modificado por oscar
    path('vista_login/', views.login,name='login'), # login/vista_login/
    path('vista_medicos/', views.vista_medico,name='vista_medico'), #login/vista_medicos/
]
