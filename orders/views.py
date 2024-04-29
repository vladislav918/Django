from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse

from .models import OrderItem
from .forms import OrderCreateForm
from .services import create_order

from cart.services import get_goods_list


class OrderCreateView(LoginRequiredMixin, CreateView):
    models = OrderItem
    form_class = OrderCreateForm
    template_name = 'orders/create.html'
    success_url = '/'


    def get_initial(self):
        initial = super().get_initial()

        initial = initial.copy()
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        initial['email'] = self.request.user.email

        return initial


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['goods'] = get_goods_list(self.request)

        return context


    def form_valid(self, form):
        create_order(self.request, form)

        return redirect(reverse('process'))
