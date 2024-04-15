from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


class ProductsView(ListView):
    model = Product
    template_name = 'goods/product_list.html'
    paginate_by = 5