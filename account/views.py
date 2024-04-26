from django.urls import reverse_lazy
from .forms import LoginUserForm, RegisterUserForm, UserPasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic.edit import CreateView



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'account/login.html'
    

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("password_change_done")
    template_name = "account/password_change_form.html"
