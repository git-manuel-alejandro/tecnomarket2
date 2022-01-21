from django.shortcuts import render
from django.template import context
from .import models

# Create your views here.

def home(request):
    productos = models.Producto.objects.all()
    context = {
        'productos' : productos
    }
    return render(request , 'productos/r_productos.html', context)

def contacto(request):
    return render(request , 'app/contacto.html')

def galeria(request):
    return render(request , 'app/galeria.html')

