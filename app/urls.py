from django import views
from django.urls import path , include
from .import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('producto' , views.ProductoViewset)

urlpatterns = [
    path('', views.home , name='home'),
    path('contacto/', views.contacto , name='contacto'),
    path('galeria/', views.galeria , name='galeria'),
    path('crearproducto/', views.crearproducto , name='crearproducto'),
    path('listarproducto/', views.listarproducto , name='listarproducto'),
    path('editarproducto/<id>/', views.editarproducto , name='editarproducto'),
    path('eliminarproducto/<id>/', views.eliminarproducto , name='eliminarproducto'),
    path('registrouser/', views.registrouser , name='registrouser'),
    path('api/', include(router.urls)),
    

]
