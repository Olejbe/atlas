# Generated by Django 3.2.7 on 2022-10-09 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoObject',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=200)),
                ('iso_a3', models.CharField(max_length=200)),
                ('geo_json', models.JSONField()),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='countries.country2')),
            ],
            options={
                'ordering': ['country_name'],
            },
        ),
    ]