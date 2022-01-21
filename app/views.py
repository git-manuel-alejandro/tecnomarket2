from django.shortcuts import render
from .import models
from .import forms

# Create your views here.

def home(request):
    productos = models.Producto.objects.all()
    context = {
        'productos' : productos
    }
    return render(request , 'productos/r_productos.html', context)

def contacto(request):
    context = {
        'form' : forms.FormContacto() 
    }

    if request.method == 'POST':
        formulario = forms.FormContacto(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            context['mensaje'] = 'contacto guardado'
        else:
            context['form'] = formulario
    return render(request , 'contactos/c_contactos.html' , context)

def galeria(request):
    return render(request , 'app/galeria.html')

