from django.db import models

from geography.models import Country
from suppliers.models import Supplier

class Category(models.Model):
    name = models.CharField(max_length=100, default='', unique=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

class Warehouse(models.Model):
    name = models.CharField(max_length=100, default='', unique=True)

    def __unicode__(self):
        return self.name

class Price(models.Model):
    MEASUREMENT_CHOICES = (
        ('sf', 'Square Feet'),
        ('mm', 'Milimetre'),
        ('u', 'Unit'),
    )
    retail_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    measurement = models.CharField(max_length=2, choices=MEASUREMENT_CHOICES, default='')

class Stock(models.Model):
    UNIT_CHOICES = (
        ('sf', 'Square Feet'),
        ('mm', 'Milimetre'),
        ('u', 'Unit'),
    )

    item_code = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=255, default='')
    category = models.ForeignKey(Category)
    retail_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    retail_unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default='', blank=True)
    wholesale_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    wholesale_unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default='', blank=True)
    dealer_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    dealer_unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default='', blank=True)
    special_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    special_unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default='', blank=True)
    pieces_per_box = models.IntegerField(null=True, blank=True, default=0)
    exempt_flag = models.BooleanField(default=False)
    nonstock_flag = models.BooleanField(default=False)
    country = models.ForeignKey(Country, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, null=True, blank=True)
