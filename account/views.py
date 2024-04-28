from django.db.models import F
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import CreateView, DetailView, ListView,UpdateView
from django.shortcuts import get_object_or_404

from account.models import CustomUser

from .forms import LoginUserForm, RegisterUserForm, UserPasswordChangeForm

from orders.models import Order


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'account/login.html'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'account/password_change_form.html'


class UserProfileDetailView(DetailView):
    model = CustomUser
    template_name = 'account/user_profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        return get_object_or_404(CustomUser, username=username)


class OrderList(ListView):
    model = Order
    template_name = 'account/user_profile_order_list.html'


    def get_queryset(self):
        return Order.objects.filter(user=self.request.user.id)


class UserProfileUpdateView(UpdateView):
    model = CustomUser
    fields = ['first_name', 'last_name']
    template_name = 'account/user_update_form.html'
    success_url = '/'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        return get_object_or_404(CustomUser, username=username)