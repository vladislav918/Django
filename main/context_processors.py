from .forms import CitySelectionForm


def choice_form(request):
    """ Выбор города """
    return {'choice_form': CitySelectionForm()}
