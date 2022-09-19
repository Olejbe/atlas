# myapi/urls.py
from django.urls import path
from api.views import World, Continents, Countries, Countries2, Continents2, Un, ListContinents

# Add new Api Urls Here
urlpatterns = [
    path('world/', World.as_view()),
    path('countries_by_continent/<str:continent>/', Continents2.as_view()),
    path('continents/', ListContinents.as_view()),
    path('country/<str:country>/', Countries.as_view()),
    path('country2/<str:country>/', Countries2.as_view()),
    path('un_members/', Un.as_view())
]