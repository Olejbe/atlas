from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render

from countries.models import Country
from maps.utils.map_creator import create_country_map


def index(request):
    queryset = Country.objects.filter(continent__name='europe').order_by('name')
    result = {'countries': [country for country in queryset]}
    return render(request, 'countries/index.html', result)


def country(request, country_name):
    try:
        country = Country.objects.prefetch_related('country').get(name_common=country_name)
        country_map = create_country_map(country, neighbours=True, capitals=True)
    except ObjectDoesNotExist:
        raise Http404("Country does not exist")
    return render(request, 'countries/details.html', {'country': country, 'map': country_map})


def continent(request, continent):

    queryset = Country.objects.filter(continent__name=continent).order_by('name_common')
    result = {'countries': [country for country in queryset], 'continent': continent.capitalize()}

    return render(request, 'countries/continent.html', result)


def home(request):
    return render(request, 'home.html')
