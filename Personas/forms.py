from django import forms
from . import models


class Medicoforms(forms.modelForm):
    run = forms.OneToOneField(
        widget = forms.textInput(
            attrs={
                'class': 'form-control'
            }
        ),
        label= 'run',
        required = True,
    )