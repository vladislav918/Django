from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('main.urls')),
    path('',include('goods.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('coupon/', include('coupons.urls')),
    path('payment/', include('payment.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
