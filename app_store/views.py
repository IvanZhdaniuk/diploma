from django.shortcuts import render
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
# Create your views here.


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny, )
    templates_name = 'categoris.html'
    def get(self, request):
        category = self.get_queryset()
        serializer = self.get_serializer(category, many=True)
        context = {'category': serializer.data}
        return render(request, self.templates_name, context)







class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny, )
    template_name = 'product_list.html'

    def get(self, request):
        products = self.get_queryset()
        serializer = self.get_serializer(products, many=True)
        context = {'products': serializer.data}
        return render(request, self.template_name, context)