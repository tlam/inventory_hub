from django.db import models

from stocks.models import Stock, Warehouse
from suppliers.models import Supplier

class ImportEntry(models.Model):
    reference_no = models.IntegerField() # automatic
    date = models.DateField()
    warehouse = models.ForeignKey(Warehouse)
    supplier = models.ForeignKey(Supplier)  # Display Foreign creditors only
    invoice_no = models.CharField(max_length=100)
    retail_price = models.DecimalField(max_digits=20, decimal_places=2)
    remarks = models.CharField(max_length=255)
    stocks = models.ManyToManyField(Stock)
    quantity = models.IntegerField()
    cost_price = models.DecimalField(max_digits=20, decimal_places=2)
    amount = models.DecimalField(max_digits=20, decimal_places=2) # quantity * cost_price
