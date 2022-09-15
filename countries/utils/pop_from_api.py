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
    for k,v in country.items():
        print(f"Key: {k}, Value: {v}, ValueTYpe: {type(v)}" )
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
        # coordinates=','.join(country['latlng']) if 'latlng' in country_keys else None,
        # capital_coordinates=','.join(country['capitalInfo']['latlng']) if 'capital' in country_keys and 'latlng' in
        #                                                                   country['capitalInfo'].keys() else None,
        # cca2=country['cca2'] if 'cca2' in country_keys else None,
        # cca3=country['cca3'] if 'cca3' in country_keys else None,
        # ccn3=country['ccn3'] if 'ccn3' in country_keys else None,
        # boders=','.join(country['borders']) if 'borders' in country_keys else None,
        # flag=country['flags']['svg']
    )
    return country_obj


def populate_countries(countries: list[dict]) -> None:
    """
    Api response with all countries in the world.
    :param countries:
    :return: None
    """
    for country in countries:
        continent = create_continent_object(country['region'])
        country_obj = create_country_object(country, continent)
        print(f"{country_obj[0].name_official} successfully created")
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



