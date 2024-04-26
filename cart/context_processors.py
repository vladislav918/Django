from .services import get_len_cart


def cart(request):
    return {'cart': get_len_cart(request)}