import folium
from countries.models import Country2
from maps.models import GeoObject
from maps.utils.markers import circle_marker, simple_marker
from maps.utils.layers import add_layers


# Rewrite this as a class at some point!!.

def extract_geo_object(country_obj: Country2) -> [GeoObject, None]:
    try:
        geo_object = country_obj.country.first()
    except Exception as e:
        print(f'An error occured when trying to fetch the geo_object, are you sure a geo object is attached? error: {e}')
        return None
    return geo_object


def add_geo_json(geo_object: GeoObject, folium_map: folium.folium.Map) -> folium.folium.Map:
    folium.GeoJson(geo_object.geo_json,
                   style_function=lambda x: {'fillColor': '#000000', 'color': '#000000'},
                   name=geo_object.country_name).add_to(folium_map)
    return folium_map


def get_neighbour_countries(country_obj: Country2) -> [list[str], None]:
    """
    Fetches the country objects for countries with a border to the selected country.
    :param country_obj:
    """
    neighbours_as_str = country_obj.borders
    print(neighbours_as_str)
    if neighbours_as_str:
        neighbours_list = country_obj.borders.split(',')
        lower_list = [n.lower() for n in neighbours_list]
        border_countries = Country2.objects.prefetch_related('country').filter(cca3__in=lower_list)
        return border_countries
    return None


def add_neighbour_countries(border_countries: list[Country2], folium_map: folium.folium.Map):
    for country in border_countries:
        geo_object = extract_geo_object(country)
        add_geo_json(geo_object, folium_map)
    return folium_map


def create_country_map(country_obj: Country2, neighbours=False, capitals=False) -> folium.folium.Map:
    geo_object = extract_geo_object(country_obj)
    m = folium.Map(location=[0, 0], zoom_start=2)
    folium.GeoJson(geo_object.geo_json, name=geo_object.country_name).add_to(m)
    if neighbours:
        border_countries = get_neighbour_countries(country_obj)
        add_neighbour_countries(border_countries, m)
    if capitals:
        # circle_marker(country_obj.capital_coordinates_lat, country_obj.capital_coordinates_lon, m)
        simple_marker(m, country_obj.capital_coordinates_lat, country_obj.capital_coordinates_lon)

    add_layers(m)
    m = m._repr_html_()
    return m






