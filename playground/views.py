# from itertools import product
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product,Customer,Collection
from store.models import Promotion
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
def say_hello(request):
    return HttpResponse("Hellow Tomi")

def teme(request):

    x=Product.objects.all()
    return render(request,'teme.html',{'productt':list(x)})

def tom(request):
    try:
        x=Product.objects.get(id=1)
        print(x)
        return render(request,'teme.html',{'x':x})
    except ObjectDoesNotExist:
        print('entry doesnt exist')

def sena(request):

    # x=Promotion.objects.filter(discount__range=(1000,5000))
    # x=Promotion.objects.filter(discount__gt=1000)
    # x=Promotion.objects.filter(discount__gt=100,description__icontains='haha')
    # x=Promotion.objects.filter(discount__lt=1000).filter(description__icontains='haha') 
    # x=Promotion.objects.filter(Q(discount__gt=1000)& Q(description__icontains='haha'))
    # x=Customer.objects.filter(first_name=F('last_name')).order_by('-birth_date')
    x=Product.objects.select_related('title').all()


    return render(request,'teme.html',{'pro':list(x)})

def lol(request):

    x=Customer.objects.filter(first_name=F('last_name'))
    return render(request,'teme.html',{'loli':list(x)})