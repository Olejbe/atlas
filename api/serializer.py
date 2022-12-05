from rest_framework import serializers
from countries.models import Country, Continent


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'population', 'land_area', 'population_density')


def country_serializer(country_object: Country) -> dict:
    """
    Serializer for the country2 model
    :param country_object:
    :return:
    """
    return {
        'name_official': country_object.name_official,
        'name_common': country_object.name_common,
        'continent': country_object.continent.name,
        'timezone': country_object.timezone,
        'independent': country_object.independent,
        'domain': country_object.domain,
        'un_member': country_object.un_member,
        'capital': country_object.capital,
        'sub_region': country_object.sub_region,
        'landlocked': country_object.landlocked,
        'population': country_object.population,
        'area': country_object.area,
        'coordinates_lat': country_object.coordinates_lat,
        'coordinates_lon': country_object.coordinates_lon,
        'capital_coordinates_lat': country_object.capital_coordinates_lat,
        'capital_coordinates_lon': country_object.capital_coordinates_lon,
        'cca2': country_object.cca2,
        'cca3': country_object.cca3,
        'ccn3': country_object.ccn3,
        'borders': country_object.borders,
        'flag': country_object.flag,
    }


def continent_serializer(continent_object: Continent) -> dict:
    return {
        'continent_name': continent_object.name
    }
