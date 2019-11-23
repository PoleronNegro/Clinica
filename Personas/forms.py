#creado por sebastian alexis

from django import forms
from . import models

class Doctor(forms.modelsForm):
    run = forms.CharField(
        widget=forms.TextInput(
            attrs ={
                'class': 'form-control'
            }
        ),
        label='Run',
        required=True,
        max_length=10
    )
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs ={
                'class': 'form-control'
            }
        ),
        label='Nombres',
        required=True,
        max_length=30
    )
    apellido = forms.CharField(
        widget=forms.TextInput(
            attrs ={
                'class': 'form-control'
            }
        ),
        label='Apellidos',
        required=True,
        max_length=30
    )
    Telefono = forms.CharField(
        widget=forms.TextInput(
            attrs ={
                'class': 'form-control'
            }
        ),
        label='Telefono',
        required=True,
        max_length=12
    )
    correo = forms.CharField(
        widget=forms.TextInput(
            attrs ={
                'class': 'form-control'
            }
        ),
        label='Correo',
        required=True,
        max_length=45
    )
    direccion= forms.CharField(
        widget=forms.TextInput(
            attrs ={
                'class': 'form-control'
            }
        ),
        label='Direccion',
        required=True,
        max_length=30
    )
    region = forms.CharField(
        widget=forms.TextInput(
            attrs= {
                'class': 'form-control'
            }
        ),
        label='Comuna',
        required=True,
        max_length=30
    )
    comuna = forms.CharField(
        widget=forms.TextInput(
            attrs ={
                'class': 'form-control'
            }
        ),
        label='Comuna',
        required=True,
        max_length=30
    )
    especialidad = forms.CharField(
        widget=forms.TextInput(
            attrs ={
                'class': 'form-control'
            }
        ),
        label='Especialidad',
        required=True,
        int(11)
    )

    class Meta:
        model =  Medico
        fields =('run',
        'nombre','apellido','telefono',
        'correo','direccion','region',
        'comuna','especialidad'
        )

    class Paciente(forms.modelsForm):
        run = forms.CharField(
        widget=forms.TextInput(
            attrs ={
                'class': 'form-control'
            }
        ),
        label='Rut Paciente',
        required=True,
        max_length=30
    )
    class Meta:
        model = Paciente
        fields=('run'
        )
    
        
