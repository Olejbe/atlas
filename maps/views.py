from django.shortcuts import render
import folium
from maps.utils.layers import add_layers
from maps.utils.read_geo import read_from_file, get_first_entry, get_entry

# Create your views here.


def world(request):
    m = folium.Map(location=[0, 0], zoom_start=2, tiles='cartodbdark_matter')
    # m = add_layers(m) # this will add all map layers specified in add_layers function.
    m=m._repr_html_()
    context = {'world_map': m}
    return render(request, 'map.html', context)


def country_map(request):
    m = folium.Map(location=[0, 0], zoom_start=2)
    all_countries_geojson = read_from_file()
    first_geojson = get_entry(all_countries_geojson, 4)
    folium.GeoJson(first_geojson).add_to(m)
    # add functionality to add country overlay
    #
    m=m._repr_html_()
    context = {'country_map': m, 'country': 'change me to country varaible when ready!'}
    return render(request, 'country_map.html', context)


