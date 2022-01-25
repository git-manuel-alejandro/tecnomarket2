from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .import models
from .import forms
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required , permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializers


class ProductoViewset(viewsets.ModelViewSet):
    queryset = models.Producto.objects.all()
    serializer_class = ProductoSerializers











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

@permission_required('app.add_producto')
def crearproducto(request):
    context = {
        'form' : forms.FormProducto() 
    }
    if request.method == 'POST':
        formulario = forms.FormProducto(data = request.POST , files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request , 'Creado correctamente')
        else:
            context['form'] = formulario

    return render(request, 'productos/crearproducto.html', context)

@permission_required('app.view_producto')
def listarproducto(request):
    productos = models.Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos , 2)  #items for page
        productos = paginator.page(page)
    except:
        raise Http404

    context = {
        'entity' : productos,
        'paginator' : paginator
    }
    return render(request, 'productos/listarproducto.html' , context)

@permission_required('app.change_producto')
def editarproducto(request , id):
    producto = get_object_or_404(models.Producto , id = id)
    data  = {
        'form' : forms.FormProducto(instance=producto)
    }
    if request.method == 'POST':
        formulario = forms.FormProducto(data = request.POST , instance = producto , files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request , 'Modificado correctamente')         
            return redirect(to = "listarproducto")
        else:
            data['form'] = formulario

    return render(request , 'productos/editarproducto.html', data)

@permission_required('app.delete_producto')
def eliminarproducto(request, id):
    producto = get_object_or_404(models.Producto , id= id)
    producto.delete()
    messages.success(request , 'Eliminado correctamente')

    return redirect(to = 'listarproducto')

def registrouser(request):
    context = {
        'form' : forms.CustumUserCreationForm() 
    }
    if request.method == 'POST':
        formulario = forms.CustumUserCreationForm(data = request.POST )
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username= formulario.cleaned_data['username'] , 
            password= formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request , 'Usuario correctamente')
            return redirect(to="home")
        else:
            context['form'] = formulario

    return render(request, 'registration/registrouser.html' , context)

