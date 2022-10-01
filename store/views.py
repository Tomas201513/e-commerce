from django.shortcuts import get_object_or_404
from  django.http import HttpRequest,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product,Order
from .serializers import ProductSerializer,OrderSerializer
from rest_framework import status 

# Create your views here.
###################### ይሄ function based view ነው ___ለመማር ይጠቅማል ብዬ አስቀምጨ ነው####################################################
# @api_view(['GET','POST'])
# def order_list(request):
    
#     if request.method=='GET':
#         all_orders=Order.objects.select_related('customer').all()
#         serializer=OrderSerializer(all_orders, many=True)
#         return Response(serializer.data)
#     elif request.method=='POST':
#         serializer=OrderSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)


# @api_view(['GET','PUT','DELETE'])
# def order(request,id):
#     order=get_object_or_404(Order, pk=id)
#     if request.method=='GET':
#         serializer=OrderSerializer(order)
#         return Response(serializer.data)
#     elif request.method=='PUT':
#         serializer=OrderSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
#     elif request.method=='DELETE':
#         order.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
##################################################################################################################################
########################################class based#######################################################################################
class OrderList(APIView):
    def get(self,reqest):
        all_orders=Order.objects.select_related('customer').all()
        serializer=OrderSerializer(all_orders, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
class OneOrder(APIView):
    def get(self,request,id):
        order=get_object_or_404(Order, pk=id)
        serializer=OrderSerializer(order)
        return Response(serializer.data)
    def put(self,request,id):
        order=get_object_or_404(Order, pk=id)
        serializer=OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    def delete(self,request,id):
        order=get_object_or_404(Order, pk=id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#####################################################################################################################################
#####################################################################################################################################











# @api_view(['GET','PUT','DELETE'])
# def product(request,id):
#     product=get_object_or_404(Product, pk=id)
#     if request.method=='GET':
#         serializer=ProductSerializer(product)
#         return Response(serializer.data)
        
#     elif request.method=='PUT':
#         serializer=ProductSerializer(product,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     elif request.method=='DELETE':
#         # if Product.promotion_set.count()>0:
#         #     return Response('eeeeeeeeeeerrrrrrrrrrrrr')
#         Product.delete()
#         return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','POST'])
# def list_product(request):

#     if request.method=='GET':
#         all_product=Product.objects.all()
#         serializer=ProductSerializer(all_product, many=True)
#         return Response(serializer.data)
        
#     elif request.method=='POST':
#         serializer=ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)







