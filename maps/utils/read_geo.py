import json
from countries.models import Country
from maps.models import GeoObject
from django.core.exceptions import ObjectDoesNotExist


def read_from_file() -> dict:
    """
    Reads from the countries geoJson file and loads them to a json object
    :return: dict
    """
    with open('countries.geojson') as geojson_file:
        data = json.load(geojson_file)
    return data

# def populate_database() -> None


def get_first_entry(data: dict) -> dict:
    """
    Just for testing purposes, but gets the first entry in the country dict.
    :param data: dict
    :return: dict
    """
    return data['features'][0]


def get_entry(data: dict, numb) -> dict:
    """
    Fetches a specified object from dict based on numering.
    :param data: dict
    :param numb: int
    :return: dict
    """
    return data['features'][numb]


def pop_db(data: dict) -> None:
    """
    Take an entire dictionary
    :param data:
    :return:
    """
    for d in data['features']:
        create_object(d)


def create_object(data: dict) -> GeoObject:
    """
    Fetches foreignKey and creates the object.
    :param data:
    :return:
    """
    geo_obj = GeoObject.objects.update_or_create(
        country=get_country_object(data['properties']['ISO_A3']),
        country_name=data['properties']['ADMIN'],
        iso_a3=data['properties']['ISO_A3'],
        geo_json=data,
    )
    return geo_obj


def get_country_object(cca3: str) -> Country:
    cca3_lower = cca3.lower()
    try:
        country_obj = Country.objects.get(cca3=cca3_lower)
    except ObjectDoesNotExist:
        print(f"found no matching country with cca3 = {cca3}")
        country_obj = None
    return country_obj


def load_geo_db() -> None:
    """
    Main function for populating the Geojson model
    :return: None
    """
    data = read_from_file()
    pop_db(data)






