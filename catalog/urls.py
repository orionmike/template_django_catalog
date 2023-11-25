from django.urls import path
from django.views.generic.base import TemplateView

from .views import *

urlpatterns = [
    path('<slug:slug>/', product_detail, name='product_detail'),
    path('cataog/', cat_category_list, name='category_list'),
    path('product-list/', product_list, name='product_list'),
    path('search/', search_product_list, name='search_product_list'),
    path('cataog/<slug:slug>/', category_detail, name='category_detail'),
]
