import folium
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render

from maps.models import GeoObject
from maps.utils.read_geo import read_from_file, get_entry


# Create your views here.


def world(request):
    m = folium.Map(location=[0, 0], zoom_start=2, tiles='cartodbdark_matter')
    # m = add_layers(m) # this will add all map layers specified in add_layers function.
    geo_objects = GeoObject.objects.all()
    for g in geo_objects:
        folium.GeoJson(g.geo_json, tooltip=g.country_name).add_to(m)
    m=m._repr_html_()
    context = {'world_map': m}
    return render(request, 'map.html', context)


def country_map(request, country):
    m = folium.Map(location=[0, 0], zoom_start=2)
    # add functionality to add country overlay
    #        country = Country2.objects.get(name_common=country_name)
    try:
        geo_obj = GeoObject.objects.get(country_name=country.capitalize())
    except ObjectDoesNotExist:
        raise Http404("Country does not exist")

    m = folium.Map(location=[0, 0], zoom_start=2)
    folium.GeoJson(geo_obj.geo_json, style_function= lambda x: {'fillColor': '#000000', 'color': '#000000'}).add_to(m)
    m=m._repr_html_()
    context = {'country_map': m, 'country': geo_obj.country_name}
    return render(request, 'country_map.html', context)


