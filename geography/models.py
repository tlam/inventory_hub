from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Cities'

    def __unicode__(self):
        return u'%s' % self.name


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Countries'

    def __unicode__(self):
        return u'%s' % self.name
