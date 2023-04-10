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
    products = Product.objects.all()
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    template_name = 'product_list.html'
    permission_classes = (AllowAny, )

    def get(self, request, slug):
        # Отфильтровываем продукты по категории
        products = self.queryset.filter(category__slug=slug)
        # Добавляем категорию в контекст
        category = Category.objects.get(slug=slug)
        context = {'products': products, 'category': category}
        return render(request, self.template_name, context)

class DetailProductListView(ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    template_name ='product_detail.html'
    permission_classes = (AllowAny, )

    def get(self, request, slug):

        product = self.get_queryset().get(slug=slug)
        serializer = self.get_serializer(product)
        context = {'product': serializer.data}
        return render(request, self.template_name, context)


class MainListView(ListAPIView):

    template_name ='main_page.html'
    permission_classes = (AllowAny, )
    def get(self, request):


        return render(request, self.template_name)

