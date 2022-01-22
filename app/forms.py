from django import forms
from .import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormContacto(forms.ModelForm):
    class Meta:
        model = models.Contacto
        fields = '__all__'


class FormProducto(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = '__all__'
        widgets = {
            "fecha_fabricacion" : forms.SelectDateWidget()
        }

class CustumUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'password1', 'password2']