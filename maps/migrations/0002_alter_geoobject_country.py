# Generated by Django 3.2.7 on 2022-10-10 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoobject',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='country', to='countries.country2'),
        ),
    ]
