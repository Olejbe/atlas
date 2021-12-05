# myapi/urls.py
from django.urls import path
from api.views import World, Continents, Countries

from countries.views import index, details,  continent


urlpatterns = [
    path('', index, name='home'),
    path('<str:name>', details, name='details'),
    # path('country/<str:country>/', Countries.as_view()),
    path('continent/<str:continent>', continent)
    #path('continent/asia', asia, name=asia),
]