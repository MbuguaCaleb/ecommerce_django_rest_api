from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from base.models import Product
from django.contrib.auth.models import User
from base.serializers import ProductSerializer

from rest_framework import status

# get all Products


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    # Data needs to be serialized before its returned to the frontend
    # when we are using the django rest framework we must serialize the data we are returning
    return Response(serializer.data)


# get Single Products
@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    # when returning one object many is set to false
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
