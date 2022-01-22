from unicodedata import name
from django import views
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home , name='home'),
    path('contacto/', views.contacto , name='contacto'),
    path('galeria/', views.galeria , name='galeria'),
    path('crearproducto/', views.crearproducto , name='crearproducto'),
    path('listarproducto/', views.listarproducto , name='listarproducto'),
    path('editarproducto/<id>/', views.editarproducto , name='editarproducto'),
    path('eliminarproducto/<id>/', views.eliminarproducto , name='eliminarproducto'),
    path('registrouser/', views.registrouser , name='registrouser'),

]
