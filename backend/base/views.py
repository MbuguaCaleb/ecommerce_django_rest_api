from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .jsondata import users
from .models import Product
from .serializers import ProductSerializer
# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


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


# token customization
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  # Customises the data inside the JWT
    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)

    #     # Add custom claims
    #     token['username'] = user.username
    #     token['message'] = "Caleb begins jwt"

    #     return token
    # customizes the response returned by JWT

    def validate(self, attrs):
        data = super().validate(attrs)

        data['username'] = self.user.username
        data['email'] = self.user.email

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    # Data needs to be serialized before its returned to the frontend
    # when we are using the django rest framework we must serialize the data we are returning
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    # when returning one object many is set to false
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
