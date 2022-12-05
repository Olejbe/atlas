# myapi/urls.py
from django.urls import path

from maps.views import world, country_map

urlpatterns = [
    path('map', world, name='map'),
    path('<str:country>', country_map, name='country_map'),
]