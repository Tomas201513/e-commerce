import collections
from unicodedata import decimal

from attr import fields
from rest_framework import serializers
from store.models import Collection, Order, Product,Customer



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['id','first_name','last_name','email','phone','birth_date','membership']
  


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['id','placed_at','payment_status','customer']
  


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','title','price','description','inventory','slug','last_update']
