import requests
from countries.models import Continent
from countries.models import Country2
from django.core.exceptions import ObjectDoesNotExist


def get_info() -> list:
    response = requests.get('https://restcountries.com/v3.1/all')
    all_countries = response.json()
    return all_countries


def fetch_continent():
    continents = ['asia', 'africa', 'europe', 'north-america', 'south-america', 'oceania']
    for continent in continents:
        Continent.objects.update_or_create(name=continent)


def create_continent_object(region: str) -> Continent:
    """
    Creates a continent object based on co
    :param region:
    :return:
    """
    try:
        obj = Continent.objects.get(name=region)
    except ObjectDoesNotExist:
        print(f'{region} does not exist therefore creating it')
        obj = Continent.objects.create(name=region)
    return obj


def create_country_object(country: dict, continent: Continent) -> Country2:
    """
    receives a country dict and continent and creates a country2 object.
    :param country:
    :param continent:
    :return: Country2
    """
    country_keys = country.keys()
    available_coordinates = True if 'latlng' in country_keys else False
    available_capital_coordinates = True if 'capital' in country_keys and 'latlng' in country[
        'capitalInfo'].keys() else False
    country_obj = Country2.objects.update_or_create(
        name_official=country['name']['official'],
        name_common=country['name']['common'],
        continent=continent,
        timezone=','.join(country["timezones"]),
        independent=country['independent'] if 'independent' in country_keys else None,
        domain=country['tld'][0] if 'tld' in country_keys else None,
        un_member=country['unMember'],
        capital=','.join(country['capital']) if 'capital' in country_keys else None,
        sub_region=country['subregion'] if 'subregion' in country_keys else None,
        landlocked=country['landlocked'],
        population=country['population'],
        area=country['area'],
        coordinates_lat=country['latlng'][0] if available_coordinates else None,
        coordinates_lon=country['latlng'][1] if available_coordinates else None,
        capital_coordinates_lat=country['capitalInfo']['latlng'][0] if available_capital_coordinates else None,
        capital_coordinates_lon=country['capitalInfo']['latlng'][1] if available_capital_coordinates else None,
        cca2=country['cca2'].lower() if 'cca2' in country_keys else None,
        cca3=country['cca3'].lower() if 'cca3' in country_keys else None,
        ccn3=country['ccn3'].lower() if 'ccn3' in country_keys else None,
        borders=','.join(country['borders']) if 'borders' in country_keys else None,
        flag=country['flags']['svg']
    )
    return country_obj


def populate_countries(countries: list[dict]) -> None:
    """
    Api response with all countries in the world.
    :param countries:
    :return: None
    """
    total_countries = len(countries)
    num=0
    for country in countries:
        continent = create_continent_object(country['region'])
        country_obj = create_country_object(country, continent)
        num+=1
        print(f"{country_obj[0].name_official} successfully {'created' if country_obj[1] else 'updated'} - {num}/{total_countries}")
        # try:
        # except Exception as e:
        #     print(f"{country['name']['official']} - failed due to the following error: {e}")


def populate_db_from_api() -> None:
    """
    Main function to run the database population.
    Fetches information from api, and then creates database entries.
    :return: None
    """
    # populate_continents()
    countries = get_info()
    populate_countries(countries)

# Remember that south africa apperantly has three capital cities -,-



