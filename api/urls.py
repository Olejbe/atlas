# myapi/urls.py
from django.urls import path
from api.views import World, Continents, Countries

# Add new Api Urls Here
urlpatterns = [
    path('world/', World.as_view()),
    path('continent/<str:continent>/', Continents.as_view()),
    path('country/<str:country>/', Countries.as_view()),
]