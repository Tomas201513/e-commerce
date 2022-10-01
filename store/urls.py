from django.urls import path
from . import views

urlpatterns=[
path('product/<id>', views.product),
path('product/', views.list_product)
,path('order/', views.order_list)
,path('order/<id>', views.order)
]