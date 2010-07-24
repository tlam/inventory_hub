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

    def __unicode__(self):
         return u'%s - %s' % (self.item_code, self.description)

    def info(self):
        if self.supplier:
            supplier_name = self.supplier.name
        else:
            supplier_name = ''

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
            'supplier': supplier_name,
        }


class StockItem(models.Model):
    stock = models.ForeignKey('stocks.Stock')
    quantity = models.IntegerField(default=0, blank=True)
    discount = models.FloatField(default=0, blank=True)
    quotation = models.ForeignKey('quotations.Quotation', blank=True, null=True)
    cash_sale = models.ForeignKey('sales.CashSale', blank=True, null=True, related_name='cash_sale')
    credit_sale = models.ForeignKey('sales.CreditSale', blank=True, null=True, related_name='credit_sale')

    def info(self):
        return {
            'stock': self.stock.__unicode__(),
            'quantity': self.quantity,
            'discount': self.discount,
        }
