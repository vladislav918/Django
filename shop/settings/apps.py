INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'crispy_forms',
    'debug_toolbar',
    'crispy_bootstrap5', 
    'dynamic_breadcrumbs',

    'main.apps.MainConfig',
    'goods.apps.GoodsConfig',
    'accounts.apps.AccountConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
    'coupons.apps.CouponsConfig',
]

INTERNAL_IPS = [
    '127.0.0.1',
]