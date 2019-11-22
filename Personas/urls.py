from django.urls import path,include
from . import views

urlpatterns = [
    #modificado por oscar
    path('vista_login/', views.login,name='login'),
]
