from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product, Cart
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
@login_required
def add_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart, created =Cart.objects.get_or_create(user=request.user)
    cart.product.add(product)
    return redirect('cart')

@login_required
def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart, created = Cart.objects.get_or_create(User=request.user)
    cart.product.remve(product)
    return redirect('cart')


@api_view(['POST'])
def process_message(request):
    message = request.data.get('message')
    # обработка сообщения
    response = {'status': 'success', 'result': 'Ответ на ваше сообщение'}
    return Response(response)

def chatbot(request):
    return render(request, 'chatbot.html')

class ContactListView(ListAPIView):
    template_name ='contact_sheet.html'
    permission_classes = (AllowAny, )
    def get(self, request):
        return render(request, self.template_name)

class NewstListView(ListAPIView):
    template_name ='news_compani.html'
    permission_classes = (AllowAny, )
    def get(self, request):
        return render(request, self.template_name)


