from django.urls import path
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView
)

from . import views


urlpatterns = [
     path('profile/orders/', views.OrderList.as_view(), name='orders_list'),
     path('profile/update/<str:username>/', views.UserProfileUpdateView.as_view(), name='user_update'),
     path('profile/<str:username>/', views.UserProfileDetailView.as_view(), name='user_profile'),
     path('login/', views.LoginUser.as_view(), name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),
     path('register/', views.RegisterUser.as_view(), name='register'),
     path('password-change/', views.UserPasswordChange.as_view(), name='password_change'),
     path('password-change/done/',
          PasswordChangeDoneView.as_view(
              template_name="accounts/password_change_done.html"),
          name='password_change_done'),
     path('password-reset/',
          PasswordResetView.as_view(
             template_name = "accounts/password_reset_form.html"),
          name='password_reset'),
     path('password-reset/done/',
          PasswordResetDoneView.as_view(
              template_name = "accounts/password_reset_done.html"),
          name='password_reset_done'),
     path('password-reset/<uidb64>/<token>/',
          PasswordResetConfirmView.as_view(
              template_name="accounts/password_reset_confirm.html"), 
          name='password_reset_confirm'),
     path('password-reset/complete/',
          PasswordResetCompleteView.as_view(
              template_name="accounts/password_reset_complete.html"),
          name='password_reset_complete'),
]
