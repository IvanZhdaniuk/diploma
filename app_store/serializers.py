
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Category, Product

from django.contrib.auth import authenticate
import datetime

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
