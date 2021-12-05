from django.db import models
from django.db.models import DO_NOTHING


class Continent(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=False)

    class Meta:
        ordering = ["name"]


class Country(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    continent = models.ForeignKey(Continent, on_delete=DO_NOTHING, null=False)
    name = models.CharField(null=False, max_length=200)
    capital = models.CharField(null=True, max_length=300)
    population = models.IntegerField(null=False)
    land_area = models.IntegerField(null=False)
    population_density = models.IntegerField(null=False)
    alpha_2 = models.CharField(null=True, max_length=2)
    alpha_3 = models.CharField(null=True, max_length=3)

    class Meta:
        ordering = ["name"]
