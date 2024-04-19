INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',
    'debug_toolbar',
    'crispy_bootstrap5', 

    'main.apps.MainConfig',
    'goods.apps.GoodsConfig',
    'account.apps.AccountConfig',
]

INTERNAL_IPS = [
    "127.0.0.1",
]