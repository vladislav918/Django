from django.urls import path
from .views import index, AboutView


urlpatterns = [
    path('', index, name='home'),
    path('about/', AboutView.as_view(), name='about'),
]
