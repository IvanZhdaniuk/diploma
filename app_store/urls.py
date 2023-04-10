

from django.urls import path
from .views import CategoryListView, ProductListView, DetailProductListView, MainListView, add_cart, remove_from_cart,\
    chatbot, ContactListView, NewstListView



urlpatterns = [
    path('main/', MainListView.as_view(), name='main'),
    path('category-all/', CategoryListView.as_view(), name='category'),
    path('products/<str:slug>/', ProductListView.as_view(), name='product_list'),
    path('detail_product/<str:slug>/', DetailProductListView.as_view(), name='detail_product_list'),
    path('add_to_cart/<str:slug>/', add_cart, name='add_to_cart'),
    path('remove-from-cart/<str:slug>/', remove_from_cart, name='remove_rom_cart'),
    path('chatbot/', chatbot, name='chatbot'),
    path('contact-list/', ContactListView.as_view(), name='contact_list'),
    path('news_compani/', NewstListView.as_view(), name='news_compani'),

]
