from django.shortcuts import render, get_object_or_404, redirect
from django.template import context
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


def crearproducto(request):
    context = {
        'form' : forms.FormProducto() 
    }
    if request.method == 'POST':
        formulario = forms.FormProducto(data = request.POST , files = request.FILES)
        if formulario.is_valid():
            formulario.save()
        else:
            context['form'] = formulario

    return render(request, 'productos/crearproducto.html', context)


def listarproducto(request):
    productos = models.Producto.objects.all()
    context = {
        'productos' : productos
    }
    return render(request, 'productos/listarproducto.html' , context)

def editarproducto(request , id):
    producto = get_object_or_404(models.Producto , id = id)
    data  = {
        'form' : forms.FormProducto(instance=producto)
    }
    if request.method == 'POST':
        formulario = forms.FormProducto(data = request.POST , instance = producto , files = request.FILES)
        if formulario.is_valid():
            formulario.save()           
            return redirect(to = "listarproducto")
        else:
            data['form'] = formulario

    return render(request , 'productos/editarproducto.html', data)


def eliminarproducto(request, id):
    producto = get_object_or_404(models.Producto , id= id)
    producto.delete()

    return redirect(to = 'listarproducto')



