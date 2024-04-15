from .models import City, Address


def choice_city(city_id):
    cities = City.objects.get(id=city_id) if city_id else City.objects.get(id=1)

    locations = Address.objects.filter(city_id=city_id)

    return cities, locations