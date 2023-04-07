
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Category, Discount, ProductItem, Producer, Promocode, \
    RegistredUser, Order, Cashback, Comment

from django.contrib.auth import authenticate
import datetime

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
