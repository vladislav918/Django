from .forms import CitySelectionForm


def choice_form(request):
    """ Выбор города """
    selected_city_id = request.session.get('selected_city')
    if selected_city_id:
        initial_data = {'city': selected_city_id}
        form = CitySelectionForm(initial=initial_data)
    else:
        form = CitySelectionForm()
    return {'choice_form': form}
