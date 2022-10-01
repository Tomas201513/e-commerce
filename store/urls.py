from django.urls import path
from . import views

urlpatterns=[
# path('product/<id>', views.product),
# path('product/', views.list_product),
path('order/', views.OrderList.as_view())
,path('order/<id>', views.OneOrder.as_view())
]