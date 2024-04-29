from django.shortcuts import redirect

from .models import Coupon
from .forms import CouponApplyForm


def coupon_apply(request):
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        coupon = Coupon.objects.filter(coupon__iexact=code).first()
        if coupon:
            request.session['coupon_id'] =  coupon.id
        else:
            request.session['coupon_id'] =  None

    return redirect('cart_detail')