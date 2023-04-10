

from django.urls import path
from .views import CategoryListView, ProductListView, DetailProductListView, MainListView




urlpatterns = [
    path('main/', MainListView.as_view(), name='main'),
    path('category-all/', CategoryListView.as_view(), name='category'),
    path('products/<str:slug>/', ProductListView.as_view(), name='product_list'),
    path('detail_product/<str:slug>/', DetailProductListView.as_view(), name='detail_product_list'),

]
