from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from countries.models import Country, Country2
from django.http import Http404


def index(request):
    queryset = Country.objects.filter(continent__name='europe').order_by('name')
    result = {'countries': [country for country in queryset]}
    return render(request, 'countries/index.html', result)


def country(request, country_name):
    try:
        country = Country2.objects.get(name_common=country_name)
    except ObjectDoesNotExist:
        raise Http404("Country does not exist")
    return render(request, 'countries/details.html', {'country': country})


def continent(request, continent):
    print(request)
    queryset = Country2.objects.filter(continent__name=continent).order_by('name_common')
    result = {'countries': [country for country in queryset], 'continent': continent.capitalize()}

    return render(request, 'countries/continent.html', result)


def home(request):
    return render(request, 'home.html')
