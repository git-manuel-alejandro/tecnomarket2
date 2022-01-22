from django import forms
from .import models

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