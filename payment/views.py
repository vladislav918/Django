from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views import View

from .services import get_checkout_session_stipe


class CreateCheckoutSessionView(View):
    def get(self, request):
        return render(request, 'payment/procces.html')


    def post(self, request):
        return redirect(get_checkout_session_stipe(request).url, code=303)


class SuccessView(TemplateView):
    template_name = 'payment/success.html'


class CancelView(TemplateView):
    template_name = 'payment/cancel.html'
