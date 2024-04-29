from django.conf import settings

from goods.models import Product


def create_or_get_session(request):
    session = request.session

    cart = session.get(settings.CART_SESSION_ID)
    if not cart:
        cart = session[settings.CART_SESSION_ID] = {}

    return cart


def add_to_cart(request, product, quantity=1):
    product_id = str(product.id)
    cart = create_or_get_session(request)
    if product_id not in cart:
        cart[product_id] = {'quantity': 0, 'price': str(product.price)}

    cart[product_id]['quantity'] += quantity

    request.session.modified = True

    return cart


def get_goods_list(request):
    cart = create_or_get_session(request)
    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)

    products_data = []
    for product in products:
        product_id = str(product.id)
        quantity = cart[product_id]['quantity']
        price = product.price
        img = product.image
        total_price = quantity * price

        product_data = {
            'id': product_id,
            'name': product.name,
            'quantity': quantity,
            'price': price,
            'total_price': total_price,
            'image': img
        }

        products_data.append(product_data)

    return products_data


def remove_goods(request, product):
    cart = create_or_get_session(request)
    product_id = str(product)

    if product_id in cart:
        del cart[product_id]

    request.session.modified = True


def get_len_cart(request):
    cart = create_or_get_session(request)
    return len(cart)


def clear_cart(request):
    del request.session[settings.CART_SESSION_ID]
    request.session.modified = True
