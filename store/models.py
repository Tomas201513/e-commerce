import imp
from itertools import count
from django.db import models
from django.urls import reverse
from django.utils.html import format_html, urlencode


class Promotion(models.Model):
    description=models.CharField( max_length=255)
    discount=models.FloatField()
    def __str__(self) -> str:
        return self.description
    class Meta:
        ordering=['description']


class Product (models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField()
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
    promotions=models.ManyToManyField(Promotion)

    def the_promotion(self):
        return ','.join([i.description for i in self.promotions.all()])

    def promotion_counts(self):
        url=(
            reverse('admin:store_promotion_changelist')
            +'?' + urlencode({ 'promotions__id':str(Promotion.id)
            })
        )
        return format_html('<a href="{}"> {} </a>',url,self.promotions.count())

             
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering=['title']



class Collection (models.Model):
    title=models.CharField(max_length=255)
    Products=models.ManyToManyField(Product)

    def the_Products(self):
        return ', '.join([i.title for i in self.Products.all()])    
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering=['title']

class Customer(models.Model):
    MEMBERSHIP_BRONZ='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'

    MEMBERSHIP_CHOICES=[
        (MEMBERSHIP_BRONZ,'Bronz'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold') ]

    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=255)
    birth_date=models.DateTimeField(null=True)
    membership=models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZ)

    def __str__(self) -> str:
        return self.first_name
    class Meta:
        db_table='store_customers'
        indexes=[
            models.Index(fields=['first_name','last_name'])
        ]
        ordering=['first_name']

class Order(models.Model):
    PAYMENT_PENDING='P'
    PAYMENT_COMPLETE='C'
    PAYMENT_FAILED='F'

    MEMBERSHIP_CHOICES=[
        (PAYMENT_PENDING,'Pending'),
        (PAYMENT_COMPLETE,'Complete'),
        (PAYMENT_FAILED,'Failed') ]
    placed_at=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=PAYMENT_PENDING)
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.payment_status
    class Meta:
        ordering=['payment_status']
class OrderItem (models.Model):
    quantity=models.PositiveSmallIntegerField()
    unit_price=models.DecimalField(max_digits=6,decimal_places=2)
    order=models.ForeignKey('Order',on_delete=models.PROTECT)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.product
    class Meta:
        ordering=['product']
class Address(models.Model):
    street=models.CharField(max_length=255)
    zip=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    Customer=models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)

    def __str__(self) -> str:
        return self.street
    class Meta:
        ordering=['street']
class Cart (models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.created_at
    class Meta:
        ordering=['created_at']
class CartItem(models.Model):
    quantity=models.PositiveSmallIntegerField()
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.cart
    class Meta:
        ordering=['cart']