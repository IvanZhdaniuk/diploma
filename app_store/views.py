from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product, Cart
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.shortcuts import render
from django.http import JsonResponse

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import QuestionForm


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



# this func send message from manager to telegram
def send_telegram(text: str):
    # token = '5730541647:AAE5TzJfqUeXuPQ6XGm7L5f7cy_nuZYHdwQ'
    newtoken = '5956279665:AAGl1G03Y2uxZmVG6-0afYujfbtuT2ySC1k'

    channel_id = '1338444137'
    url = f"https://api.telegram.org/bot{newtoken}/sendMessage?chat_id={channel_id}&text={text}"
    print(requests.get(url))  # Эта строка отсылает сообщение


# this func read the form and
def chatbot(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            send_telegram('У вас новый вопрос: ' + str(form.cleaned_data['question']) + ' от '+ str(form.cleaned_data['name']) + ' нужно перезвонить на номер: '+str(form.cleaned_data['mobile_phone']))
            # create sending messages from telegram
            return HttpResponseRedirect('/store/category-all/')
    return render(request, 'chatbot.html', {'form': form})



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



def send_message_to_bot(message):
    bot_token = '5730541647:AAE5TzJfqUeXuPQ6XGm7L5f7cy_nuZYHdwQ'
    chat_id = '173901673,124543434,143343455'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
    response = requests.get(url)
    return response.json()

def send_message(request):
    if request.method == "POST":
        message = request.POST.get("message")
        # Perform some action with user input and get response from manager
        response = "Response from manager"
        send_message_to_bot(response)
        return JsonResponse(response, safe=False)
    return render(request, "chatbot.html")


