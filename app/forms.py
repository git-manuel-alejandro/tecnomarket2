from django import forms
from .import models

class FormContacto(forms.ModelForm):
    class Meta:
        model = models.Contacto
        fields = '__all__'