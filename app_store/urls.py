

from django.urls import path
from .views import CategoryListView, ProductListView




urlpatterns = [
    path('category-all/', CategoryListView.as_view()),
    path('products/<str:slug>/', ProductListView.as_view(), name='product_list'),

]
