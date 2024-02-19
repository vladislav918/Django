from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Address


def index(request):
    return render(request, 'main/main.html')


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        locations = Address.objects.all()
        context['locations'] = locations
        return context
