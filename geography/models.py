from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Cities'

class Country(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Geographies'
