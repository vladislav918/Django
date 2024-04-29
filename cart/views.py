from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from goods.models import Product

from .forms import CartAddProductForm
from .services import add_to_cart, get_goods_list, remove_goods


class CartAddView(LoginRequiredMixin, View):

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)

        if form.is_valid():
            add_to_cart(request, product=product, quantity=form.cleaned_data['quantity'])

        return redirect('/')


class CartDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'cart/cart_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['goods'] = get_goods_list(self.request)

        return context


class CartRemoveView(LoginRequiredMixin, View):

    def post(self, request, product_id):
        remove_goods(request, product_id)
        return redirect('cart_detail')
