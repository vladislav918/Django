from django.urls import path
from .views import ProductsView, ProductDetalView, CommentCreateView


urlpatterns = [
    path('', ProductsView.as_view(), name='home'),
    path('<slug:slug>',ProductDetalView.as_view(),name='product_detail'),
    path('comment/', CommentCreateView.as_view(), name='comment_form'),
]
