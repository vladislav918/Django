from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView


from .forms import CitySelectionForm, ContactForm
from .models import Address, City


def index(request):
    return render(request, 'main/main.html')


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        selected_city_id = self.request.session.get('selected_city')
        if selected_city_id:
            cities = City.objects.get(id=selected_city_id)
        else:
            cities = City.objects.get(id=1)

        locations = Address.objects.filter(city_id=selected_city_id)
        form = ContactForm()

        context['locations'] = locations
        context['form'] = form
        context['cities'] = cities
        return context


class CreateContact(CreateView):
    form_class = ContactForm
    success_url = '/about'


def city_selection(request):
    if request.method == 'POST':
        form = CitySelectionForm(request.POST)
        if form.is_valid():
            selected_city = form.cleaned_data['city']
            request.session['selected_city'] = selected_city.id
            return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = CitySelectionForm()
    return render(request, 'main/city.html', {'form': form})
