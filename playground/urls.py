from django.urls import path
from . import views

urlpatterns=[
path('hello/', views.say_hello),
path('teme/', views.teme),
path('tom/', views.tom),
path('sena/', views.sena),
path('lol/', views.lol),
path('full_name/', views.full_name),


]