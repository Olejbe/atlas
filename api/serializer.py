from rest_framework import serializers
from countries.models import Country


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'population', 'land_area', 'population_density')


def country_serializer(country_object: Country) -> dict:
    """
    formats and serializes the country object
    """
    return {
        'name': country_object.name.capitalize(), # Fix this so all countires are Capitalized in DB.
        'capital': country_object.capital,
        'population': country_object.population,
        'land_area': country_object.land_area,
        'population_density': country_object.population_density,
        'alpha_3': country_object.alpha_3.upper(),
        'flag_url': f'https://flagcdn.com/192x144/{country_object.alpha_2}.png'
    }