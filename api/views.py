from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from api.serializer import country_serializer, continent_serializer
from countries.models import Country, Continent


class Continents(APIView):
    def get(self, request, continent) -> Response:
        if continent.lower() not in ['asia', 'africa', 'europe', 'north-america', 'south-america', 'oceania']:
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
            return Response({'status': "not Found", "message": f"{country} is not a valid country"},
                            status=HTTP_404_NOT_FOUND)
        elif len(c) > 1:
            return Response({"Status": "multiple occurences", "message": f"More than one occurence, be more spesific "},
                            status=HTTP_400_BAD_REQUEST)
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
            return Response({'status': "not Found", "message": f"{filter} is not a valid filter"},
                            status=HTTP_400_BAD_REQUEST)


class Countries2(APIView):
    def get(self, request, country) -> Response:
        c = Country.objects.filter(name_common=country)
        if not c:
            return Response({'status': "not Found", "message": f"{country} is not a valid country"},
                            status=HTTP_404_NOT_FOUND)
        elif len(c) > 1:
            return Response({"Status": "multiple occurences", "message": f"More than one occurence, be more spesific "},
                            status=HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": "success", 'data': country_serializer(c.first())}, status=HTTP_200_OK)


class Un(APIView):
    def get(self, request) -> Response:
        un_members = Country.objects.filter(un_member=True)
        return Response({"status": "success", 'data': [country_serializer(un_member) for un_member in un_members]}, status=HTTP_200_OK)


class Continents2(APIView):
    def get(self, request, continent) -> Response:

        if continent.lower() not in [c[0].lower() for c in Continent.objects.values_list('name')]:
            return Response({"message": f"{continent} is not a valid continent"}, status=HTTP_404_NOT_FOUND)
        queryset = Country.objects.filter(continent__name=continent.capitalize()).order_by('name_common')
        numb_countries = len(queryset)
        sum_population = Country.objects.filter(continent__name=continent).aggregate(Sum('population'))
        total_population = sum_population['population__sum']
        result = [country_serializer(country) for country in queryset]

        return Response({"status": "success", 'number_of_countries': numb_countries,
                         'population': total_population, 'data': result}, status=HTTP_200_OK)


class ListContinents(APIView):
    def get(self, request):
        try:
            continents = Continent.objects.all()
            return Response({"status": "success", 'data': [continent_serializer(continent) for continent in continents]}, status=HTTP_200_OK)
        except Exception as e:
            return Response({"Status": "error", "message": f"something went wrong when fetching continents",
                             "error": e.__str__()},
                            status=HTTP_400_BAD_REQUEST)