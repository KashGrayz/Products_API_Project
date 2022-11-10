from rest_framework import serializers
from .models import Product

class ProductSerialiszer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'discription', 'price', 'inventory_quantity']