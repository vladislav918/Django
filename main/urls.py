from django.urls import path
from .views import index, AboutView, city_selection, CreateContact


urlpatterns = [
    path('', index, name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('city-selection/', city_selection, name='city_selection'),
    path('feedback/', CreateContact.as_view(), name="feedback"),
]
