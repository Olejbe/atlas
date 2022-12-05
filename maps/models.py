from django.db import models
from django.db.models import DO_NOTHING

from countries.models import Country

# Create your models here.


class GeoObject(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    country = models.ForeignKey(Country, on_delete=DO_NOTHING, null=True, related_name='country')
    country_name = models.CharField(null=False, max_length=200)
    iso_a3 = models.CharField(null=False, max_length=200)
    geo_json = models.JSONField()

    class Meta:
        ordering = ["country_name"]