from django.shortcuts import render
from .serializers import CategorySerializer
from .models import Category
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
# Create your views here.


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny, )