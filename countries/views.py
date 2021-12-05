from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from countries.models import Country
from django.http import Http404


def index(request):
    queryset = Country.objects.filter(continent__name='europe').order_by('name')
    result = {'countries': [country for country in queryset]}
    return render(request, 'countries/index.html', result)


def details(request, name):
    try:
        country = Country.objects.get(name=name)
    except ObjectDoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'countries/details.html', {'country': country})


def continent(request, continent):
    queryset = Country.objects.filter(continent__name=continent).order_by('name')
    hurra = {'countries': [country for country in queryset], 'continent': continent}
    return render(request, 'countries/continent.html', hurra)