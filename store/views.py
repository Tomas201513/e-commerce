from django.shortcuts import get_object_or_404
from  django.http import HttpRequest,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,Order
from .serializers import ProductSerializer,OrderSerializer
from rest_framework import status 

# Create your views here.
@api_view(['GET','PUT','DELETE'])
def product(request,id):
    product=get_object_or_404(Product, pk=id)
    if request.method=='GET':
        serializer=ProductSerializer(product)
        return Response(serializer.data)
        
    elif request.method=='PUT':
        serializer=ProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    elif request.method=='DELETE':
        if Product.OrderItem.count()>0:
            return Response('eeeeeeeeeeerrrrrrrrrrrrr')
        Product.delete()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def list_product(request):

    if request.method=='GET':
        all_product=Product.objects.all()
        serializer=ProductSerializer(all_product, many=True)
        return Response(serializer.data)
        
    elif request.method=='POST':
        serializer=ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)



@api_view()
def order_list(request):
    all_orders=Order.objects.select_related('customer').all()
    serializer=OrderSerializer(all_orders, many=True)
    return Response(serializer.data)