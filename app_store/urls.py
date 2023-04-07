

from django.urls import path
from .views import CategoryListView, ProductListView


urlpatterns = [
    path('category-all/', CategoryListView.as_view()),
    path('product-all/', ProductListView.as_view()),

]
