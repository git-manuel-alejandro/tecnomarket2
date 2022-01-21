from django.contrib import admin
from .import models

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'nuevo', 'marca', 'imagen']
    list_editable = ['precio']
    search_fields = ['nombre ']
    list_filter = ['nuevo', 'nombre', 'marca']
    list_per_page = 1

admin.site.register(models.Marca)
admin.site.register(models.Producto , ProductoAdmin)
