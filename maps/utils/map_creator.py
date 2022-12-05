import folium
from countries.models import Country2
from maps.models import GeoObject
from maps.utils.markers import circle_marker, simple_capital_marker
from maps.utils.layers import add_layers


# Rewrite this as a class at some point!!.

def extract_geo_object(country_obj: Country2) -> [GeoObject, None]:
    try:
        geo_object = country_obj.country.first()
    except Exception as e:
        print(
            f'An error occurred when trying to fetch the geo_object, are you sure a geo object is attached? error: {e}')
        return None
    return geo_object


def generate_tooltip(country: Country2) -> str:
    tooltip = f'<div style="width:95%;text-align:center">' \
              f'<img src="https://flagcdn.com/48x36/{country.cca2}.png" alt="{country.name_common}">' \
              f'<h4 style=text>{country.name_common}</h4>' \
              f'</div>'
    return tooltip

#investigate this a bit.
def add_tooltip_geo_json(geo_json:folium.GeoJson) -> None:
    folium.GeoJsonTooltip(

    ).add_to(geo_json)


def add_geo_json(country: Country2, geo_object: GeoObject, folium_map: folium.folium.Map) -> folium.folium.Map:
    tooltip = generate_tooltip(country)
    geo_json = folium.GeoJson(geo_object.geo_json,
                   style_function=lambda x: {'fillColor': '#000000', 'color': '#000000'},
                   name=geo_object.country_name,
                   tooltip=f'{tooltip}',
                   popup='lol').add_to(folium_map)

    return folium_map


def get_neighbour_countries(country_obj: Country2) -> [list[str], None]:
    """
    Fetches the country objects for countries with a border to the selected country.
    :param country_obj:
    """
    neighbours_as_str = country_obj.borders
    if neighbours_as_str:
        neighbours_list = country_obj.borders.split(',')
        lower_list = [n.lower() for n in neighbours_list]
        border_countries = Country2.objects.prefetch_related('country').filter(cca3__in=lower_list)
        return border_countries
    return None


def add_neighbour_countries(border_countries: list[Country2], folium_map: folium.folium.Map):
    for country in border_countries:
        geo_object = extract_geo_object(country)
        add_geo_json(country, geo_object, folium_map)
    return folium_map


def create_country_map(country_obj: Country2, neighbours=False, capitals=False) -> folium.folium.Map:
    geo_object = extract_geo_object(country_obj)
    lon = country_obj.capital_coordinates_lon
    lat = country_obj.capital_coordinates_lat
    m = folium.Map(location=[lat, lon], zoom_start=3)
    folium.GeoJson(geo_object.geo_json, name=geo_object.country_name).add_to(m)
    border_countries = get_neighbour_countries(country_obj)
    if neighbours and border_countries:
        add_neighbour_countries(border_countries, m)
    if capitals:
        # circle_marker(country_obj.capital_coordinates_lat, country_obj.capital_coordinates_lon, m)
        simple_capital_marker(m, country_obj)

    add_layers(m)
    m = m._repr_html_()
    return m


# class MapGenerator:
#
#     def __init__(self, country_obj):
#         self.country_obj = country_obj
#         self.map = None
#         self.neighbours = None
#         self.zoom_start = 3
#
#     def generate_map(self, lat=None, lon=None):
#         if not lat or lon:
#             lat = self.country_obj.country_obj.capital_coordinates_lat
#             lon = self.country_obj. country_obj.capital_coordinates_lon
#
#         self.map = folium.Map(location=[lat, lon], zoom_start=self.zoom_start)
#
#     def extrac_neighbours(self):
#         if self.country_obj.borders:
#             neighbours_list = self.country_obj.borders.split(',')
#             lower_list = [n.lower() for n in neighbours_list]
#             self.neighbours = Country2.objects.prefetch_related('country').filter(cca3__in=lower_list)
#
#     def add_
#
#     def add_geo_json(self):
#         folium.GeoJson(geo_object.geo_json,
#                        style_function=lambda x: {'fillColor': '#000000', 'color': '#000000'},
#                        name=geo_object.country_name,
#                        tooltip='<img src="https://flagcdn.com/256x192/fi.png" alt="Finland">',
#                        popup='lol').add_to(folium_map)


