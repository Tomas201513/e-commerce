from django.shortcuts import get_object_or_404
from  django.http import HttpRequest,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,Order
from .serializers import ProductSerializer,OrderSerializer
from rest_framework import status 
# Create your views here.
@api_view(['GET'])
def product(request,id):
    # product=Product.objects.get(pk=id)
    product=get_object_or_404(Product, pk=id)
    serializer=ProductSerializer(product)
    return Response(serializer.data)

@api_view()
def list_product(request):
    all_product=Product.objects.all()
    serializer=ProductSerializer(all_product, many=True)
    return Response(serializer.data)
@api_view()
def order_list(request):
    all_orders=Order.objects.select_related('customer').all()
    serializer=OrderSerializer(all_orders, many=True)
    return Response(serializer.data)