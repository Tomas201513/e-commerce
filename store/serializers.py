import collections
from unicodedata import decimal
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
    id=serializers.IntegerField()
    title=serializers.CharField(max_length=255)
    price=serializers.DecimalField(max_digits=6, decimal_places=2)
    

class OrderSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    placed_at=serializers.DateTimeField()
    payment_status=serializers.CharField()
    customer=CustomerSerializer()


 