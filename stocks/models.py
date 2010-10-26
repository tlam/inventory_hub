from django.db import models

from geography.models import Country
from sales.models import CashSale, CreditSale
from suppliers.models import ForeignSupplier, LocalSupplier


class Category(models.Model):
    name = models.CharField(max_length=100, default='', unique=True)
    code = models.CharField(max_length=10, default='')
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return u'%s - %s' % (self.code, self.name)


class Colour(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return u'%s' % self.name


class Stock(models.Model):
    SQUARE_FEET = 'SF'
    SQUARE_METRE = 'SM'
    UNIT = 'U'
    UNIT_CHOICES = (
        (SQUARE_FEET, 'Square Feet'),
        (SQUARE_METRE, 'Square Metre'),
        (UNIT, 'Unit'),
    )

    item_code = models.CharField(max_length=50, unique=True)
    item_name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, default='')
    colour = models.ForeignKey(Colour, null=True, blank=True)
    size = models.CharField(max_length=50, blank=True)
    tonality = models.CharField(max_length=5, blank=True)
    caliber = models.CharField(max_length=5, blank=True)
    category = models.ForeignKey(Category)
    retail_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    retail_unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default=UNIT)
    wholesale_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    wholesale_unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default=UNIT)
    dealer_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    dealer_unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default=UNIT)
    special_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    special_unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default=UNIT)
    pieces_per_box = models.IntegerField(null=True, blank=True, default=0)
    exempt_flag = models.BooleanField(default=False)
    nonstock_flag = models.BooleanField(default=False)
    country = models.ForeignKey(Country, null=True, blank=True)

    def __unicode__(self):
         return u'%s - %s' % (self.item_code, self.description)

    def info(self):
        if self.country:
            country_name = self.country.name
        else:
            country_name = ''

        return {
            'item_code': self.item_code,
            'description': self.description,
            'category': self.category.name,
            'retail_price': '%.2f' % self.retail_price,
            'retail_unit': self.retail_unit,
            'wholesale_price': '%.2f' % self.wholesale_price,
            'wholesale_unit': self.wholesale_unit,
            'dealer_price': '%.2f' % self.dealer_price,
            'dealer_unit': self.dealer_unit,
            'special_price': '%.2f' % self.special_price,
            'special_unit': self.special_unit,
            'pieces_per_box': self.pieces_per_box,
            'exempt_flag': self.exempt_flag,
            'nonstock_flag': self.nonstock_flag,
            'country': country_name,
        }

    def customer_price(self, price_type):
        if price_type == 'R':
            return self.retail_price
        elif price_type == 'W':
            return self.wholesale_price
        elif price_type == 'D':
            return self.dealer_price
        else:
            return self.special_price
