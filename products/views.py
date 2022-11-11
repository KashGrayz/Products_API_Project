from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerialiszer
from .models import Product

@api_view(['GET', 'POST'])   #Object Inquiry and Create Function
def products_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerialiszer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerialiszer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE']) #Object Inguiry by Pk
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        serializer = ProductSerialiszer(product);
        return Response (serializer.data)
    
    elif request.method == 'PUT': #Object Update
        serializer = ProductSerialiszer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE': #Object Delete
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
