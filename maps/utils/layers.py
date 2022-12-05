import folium


def add_layers(m: folium.folium.Map) -> folium.folium.Map:
    """
    Adds layers to the map.
    :param m: the map object
    :return: map object with layers
    """
    folium.TileLayer('Stamen Terrain').add_to(m)
    folium.TileLayer('Stamen Toner').add_to(m)
    folium.TileLayer('Stamen Water Color').add_to(m)
    folium.TileLayer('cartodbpositron').add_to(m)
    folium.TileLayer('cartodbdark_matter').add_to(m)
    folium.LayerControl().add_to(m)
    return m