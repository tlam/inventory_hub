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


class Stock(models.Model):
    SQUARE_FEET = 'SF'
    SQUARE_METRE = 'SM'
    UNIT = 'U'
    UNIT_CHOICES = (
        (SQUARE_FEET, 'Square Feet'),
        (SQUARE_METRE, 'Square Metre'),
        (UNIT, 'Unit'),
    )

    item_code = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=255, default='')
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
    foreign_supplier = models.ForeignKey(ForeignSupplier, null=True, blank=True)
    local_supplier = models.ForeignKey(LocalSupplier, null=True, blank=True)

    def __unicode__(self):
         return u'%s - %s' % (self.item_code, self.description)

    def info(self):
        if self.foreign_supplier:
            foreign_supplier_name = self.foreign_supplier
        else:
            foreign_supplier_name = ''

        if self.local_supplier:
            local_supplier_name = self.local_supplier
        else:
            local_supplier_name = ''

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
            'foreign_supplier': foreign_supplier_name,
            'local_supplier': local_supplier_name,
        }


class StockItemManager(models.Manager):
    def items_for(self, generic_object):
        if isinstance(generic_object, CashSale):
            return StockItem.objects.filter(cash_sale=generic_object)
        elif isinstance(generic_object, CreditSale):
            return StockItem.objects.filter(credit_sale=generic_object)
        else:
            return StockItem.objects.filter(quotation=generic_object)

    def items_info(self, sale):
        stock_items = self.items_for(sale)
        history_dict = {}
        for item in stock_items:
            history_dict[item.id] = item.info()
        return history_dict


class StockItem(models.Model):
    stock = models.ForeignKey('stocks.Stock')
    quantity = models.IntegerField(default=0, blank=True)
    discount = models.FloatField(default=0, blank=True)
    quotation = models.ForeignKey('quotations.Quotation', blank=True, null=True)
    cash_sale = models.ForeignKey('sales.CashSale', blank=True, null=True, related_name='cash_sale')
    credit_sale = models.ForeignKey('sales.CreditSale', blank=True, null=True, related_name='credit_sale')
    objects = StockItemManager()

    def info(self):
        data = {
            'stock': self.stock.__unicode__(),
            'quantity': self.quantity,
            'discount': self.discount,
        }

        if self.quotation:
            data['quotation'] = self.quotation.__unicode__()

        if self.cash_sale:
            data['cash_sale'] = self.cash_sale.__unicode__()

        if self.credit_sale:
            data['credit_sale'] = self.credit_sale.__unicode__()

        return data
