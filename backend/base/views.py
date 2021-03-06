from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .jsondata import users
from .models import Product
from django.contrib.auth.models import User
from .serializers import ProductSerializer, UserSerializer, UserSerializerWithToken
# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status
# token customization


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # @classmethod   # Customises the data inside the JWT

    # def get_token(cls, user):
    #     token = super().get_token(user)

    #     # Add custom claims
    #     token['username'] = user.username
    #     token['message'] = "Caleb begins jwt"

    #     return token

    def validate(self, attrs):     # customizes the response returned by JWT

        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerUser(request):
    data = request.data

    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

       # because i am only returning only one user
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)

    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

        # Get user profile


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


# Get all the system users
@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)


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
