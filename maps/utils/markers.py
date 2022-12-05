import folium
from countries.models import Country2

def add_marker(m: folium.folium.Map, lat: float =None, lon: float=None, color: str=None) -> folium.folium.Map:
    """

    :param m: the map object
    :param lat: latitude of the marker
    :param lon: longitude of the marker
    :param color: the color of the marker, defaults to blue
    :return: a folium map object
    """
    if not lat or not lon:
        lat = 59.9
        lon = 10.75

    if not color:
        color = 'blue'

    folium.Marker(location=[lat, lon],
                  popup='Custom Marker 2',
                  tooltip='<strong>Click here to see Popup</strong>',
                  icon=folium.Icon(color=color, prefix='glyphicon', icon='off')
                  ).add_to(m)
    return m

# This needs more development

def simple_capital_marker(m:folium.folium.Map, country:Country2) -> folium.folium.Map:
    """
    :param m: the map object
    :param lat: latitude
    :param lon: longitude
    :return: folium object with marker attached.
    """
    lat = country.capital_coordinates_lat
    lon = country.capital_coordinates_lon
    tooltip = country.capital
    folium.Marker(location=[lat, lon],
                  # popup='Custom Marker 2',
                  tooltip=f'{tooltip}',
                  icon=folium.Icon(prefix='glyphicon', icon='off')
                  ).add_to(m)
    return m


def circle_marker(lat: float, lon: float, folium_map: folium.folium.Map) -> folium.folium.Map:
    folium.CircleMarker(
        location=(lat, lon),
        radius=10,
        popup="Laurelhurst Park",
        color="#3186cc",
        fill=True,
        # fill_color="#3186cc",
        fill_color="darkred",
    ).add_to(folium_map)
    return folium_map

