import collections
from unicodedata import decimal

from attr import fields
from rest_framework import serializers
from store.models import Product,Customer


class CustomerSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    first_name=serializers.CharField(max_length=255)
    last_name=serializers.CharField(max_length=255)
    email=serializers.EmailField()
    phone=serializers.CharField(max_length=255)
    birth_date=serializers.DateTimeField()
    membership=serializers.CharField()

class ProductSerializer(serializers.Serializer):
    class meta:
        model=Product
        fields=['id','title','slug','description','price','inventory']
    



class OrderSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    placed_at=serializers.DateTimeField()
    payment_status=serializers.CharField()
    customer=CustomerSerializer()


 