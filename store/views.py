from django.shortcuts import render
from  django.http import HttpRequest,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view()
def list_product(request,id):
    return Response(id)
