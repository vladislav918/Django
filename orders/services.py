from cart.services import get_goods_list, clear_cart
from .models import OrderItem

from goods.models import Product


def create_order(request, form):
    order = form.save(commit=False)
    order.user = request.user
    order.save()

    cart = get_goods_list(request)
    products = Product.objects.in_bulk([item['id'] for item in cart])
    for item in cart:
        product = products.get(int(item['id']))
        if product:
            OrderItem.objects.create(
                order=order,
                product=product,
                price=item['price'],
                quantity=item['quantity']
            )

    request.session['order_id'] = order.id

    clear_cart(request)
