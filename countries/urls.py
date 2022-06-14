# myapi/urls.py
from django.urls import path
from api.views import World, Continents, Countries

from countries.views import home, country, continent


urlpatterns = [
    # path('', index, name='home'),
    path('', home, name='home'),
    path('<str:country_name>', country, name='country'),
    # path('country/<str:country>/', Countries.as_view()),
    path('continent/<str:continent>', continent)
    #path('continent/asia', asia, name=asia),
]