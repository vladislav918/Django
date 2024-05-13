import stripe
from django.conf import settings
from orders.models import Order
from django.shortcuts import get_object_or_404

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_checkout_session_stipe(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)
    domain = "http://0.0.0.0:8000"
    line_items = []
    for item in order.items.all():
        line_items.append({
            'price_data': {
                'unit_amount': int(item.price * 100),
                'currency': 'usd',
                'product_data': {
                    'name': item.product.name,
                },
            },
            'quantity': item.quantity,
        })
    checkout_session = stripe.checkout.Session.create(
        customer_email=request.user.email,
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        metadata={'order_id': order_id},
        success_url=domain + '/payment/success/',
        cancel_url=domain + '/payment/cancel/',
    )
    return checkout_session
