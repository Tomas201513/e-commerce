from django.urls import path
from . import views

urlpatterns=[
path('list_product/<id>', views.list_product)
]