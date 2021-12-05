from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from api.serializer import country_serializer
from countries.models import Country


class Continents(APIView):
    def get(self, request, continent) -> Response:
        if continent.lower() not in ['asia', 'africa', 'europe', 'north-america', 'south-america','oceania']:
            return Response({"message": f"{continent} is not a valid continent"}, status=HTTP_404_NOT_FOUND)
        queryset = Country.objects.filter(continent__name=continent).order_by('name')
        numb_countries = len(queryset)
        sum_population = Country.objects.filter(continent__name=continent).aggregate(Sum('population'))
        total_population = sum_population['population__sum']
        result = [country_serializer(country) for country in queryset]

        return Response({"status": "success", 'number_of_countries': numb_countries,
                         'population': total_population, 'data': result}, status=HTTP_200_OK)


class Countries(APIView):
    def get(self, request, country) -> Response:
        c = Country.objects.filter(name=country)
        if not c:
            return Response({'status': "not Found", "message": f"{country} is not a valid country"}, status=HTTP_404_NOT_FOUND)
        elif len(c) > 1:
            return Response({"Status": "multiple occurences", "message": f"More than one occurence, be more spesific "}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": "success", 'data': country_serializer(c.first())}, status=HTTP_200_OK)


class World(APIView):
    def get(self, request) -> Response:
        queryset = Country.objects.all().order_by('name')
        numb_countries = len(queryset)
        sum_population = Country.objects.all().aggregate(Sum('population'))
        total_population = sum_population['population__sum']
        result = [country_serializer(country) for country in queryset]
        return Response({"status": "success", 'number_of_countries': numb_countries,
                         'population': total_population, 'data': result}, status=HTTP_200_OK)


class Top(APIView):
    def get(self, request, filter) -> Response:
        if filter.lower() not in ['population', 'area', 'density']:
            return Response({'status': "not Found", "message": f"{filter} is not a valid filter"}, status=HTTP_400_BAD_REQUEST)


