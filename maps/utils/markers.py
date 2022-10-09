import folium

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
def simple_marker(m:folium.folium.Map, lat, lon) -> folium.folium.Map:
    """
    :param m: the map object
    :param lat: latitude
    :param lon: longitude
    :return: folium object with marker attached.
    """
    folium.Marker(location=[lat, lon],
                  popup='Custom Marker 2',
                  tooltip='<strong>Click here to see Popup</strong>',
                  icon=folium.Icon(prefix='glyphicon', icon='off')
                  ).add_to(m)
    return m