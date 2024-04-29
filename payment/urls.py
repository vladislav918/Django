from django.urls import path

from .views import (
    CreateCheckoutSessionView,
    CancelView,
    SuccessView,
)


urlpatterns = [
    path('process/', CreateCheckoutSessionView.as_view(), name='process'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
]
