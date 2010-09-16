from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=100, default='', unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name
