from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product


# Wraps around my model to return back Json data
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # serializing all the fields at once
