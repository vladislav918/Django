from django.urls import path
from .views import AboutView, CitySelectionFormView, CreateContact


urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('city-selection/', CitySelectionFormView.as_view(), name='city_selection'),
    path('feedback/', CreateContact.as_view(), name="feedback"),
]
