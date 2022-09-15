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


class Country2(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    continent = models.ForeignKey(Continent, on_delete=DO_NOTHING, null=False)
    name_official = models.CharField(null=False, max_length=200)
    name_common = models.CharField(null=False, max_length=200)
    timezone = models.CharField(null=False, max_length=200)
    independent = models.BooleanField(null=True)
    domain = models.CharField(null=True, max_length=200)
    un_member = models.BooleanField(null=False)
    capital = models.CharField(null=True, max_length=200)
    sub_region = models.CharField(null=True, max_length=200)
    landlocked = models.BooleanField(null=False)
    population = models.IntegerField(null=False)
    area = models.FloatField(null=False)
    coordinates = models.FloatField(null=True)
    capital_coordinates = models.FloatField(null=True)
    cca2 = models.CharField(null=True, max_length=200)
    cca3 = models.CharField(null=True, max_length=200)
    ccn3 = models.CharField(null=True, max_length=200)
    borders = models.CharField(null=True, max_length=200)
    flag = models.CharField(null=True, max_length=200)

    class Meta:
        ordering = ['name_official']