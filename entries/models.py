from django.db import models

from stocks.models import Stock
from suppliers.models import ForeignSupplier
from warehouses.models import Warehouse


class ImportEntry(models.Model):
    reference_no = models.IntegerField() # automatic
    date = models.DateField()
    warehouse = models.ForeignKey(Warehouse)
    foreign_supplier = models.ForeignKey(ForeignSupplier)
    invoice_no = models.CharField(max_length=100)
    retail_price = models.DecimalField(max_digits=20, decimal_places=2)
    remarks = models.CharField(max_length=255)
    stocks = models.ManyToManyField(Stock)
    quantity = models.IntegerField()
    cost_price = models.DecimalField(max_digits=20, decimal_places=2)
    amount = models.DecimalField(max_digits=20, decimal_places=2) # quantity * cost_price

    class Meta:
        verbose_name_plural = 'Import entries'
