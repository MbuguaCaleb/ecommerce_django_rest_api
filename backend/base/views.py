from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .jsondata import users
# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/products/',
        '/api/products/create',
        '/api/products/upload',
        '/api/products/<id>/reviews/',
        '/api/products/top/',
        '/api/products/<id>/',
        '/api/products/delete/<id>',
        '/api/products/<update>/<id>/',
    ]

    return Response(routes)


@api_view(['GET'])
def getProducts(request):
    return Response(users)


@api_view(['GET'])
def getProduct(request, pk):
    user = None
    for i in users:
        if i['userId'] == pk:
            user = i
            break
    return Response(user)
