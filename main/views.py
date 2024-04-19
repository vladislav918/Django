from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from .models import ContactModel
from .forms import CitySelectionForm, ContactForm
from .services import choice_city


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        selected_city_id = self.request.session.get('selected_city')
        cities, locations = choice_city(selected_city_id)

        context['locations'] = locations
        context['form'] = ContactForm()
        context['cities'] = cities
        return context


class CreateContact(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    success_url = '/about/'
    success_message = "Сообщение отправлено"



class CitySelectionFormView(FormView):
    template_name = "main/city.html"
    form_class = CitySelectionForm
    success_url = '/about/'

    def form_valid(self, form):
        selected_city = form.cleaned_data['city']
        self.request.session['selected_city'] = selected_city.id
        return redirect(self.request.META.get('HTTP_REFERER', '/'))
