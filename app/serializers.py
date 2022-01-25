from .import models
from rest_framework import serializers

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Producto
        fields = '__all__'