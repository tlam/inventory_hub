from django.db import models

class ImportEntry(models.Model):
    reference_no = models.IntegerField() # automatic
    date = models.DateField()
    warehouse = models.ForeignKey(Warehouse)
    supplier = models.ForeignKey(Supplier)  # Display Foreign creditors only
    invoice_no = models.CharField(max=100)
    retail_price = models.DecimalField(max_digits=20, decimal=2)
    remarks = models.CharField(max=255)
    stocks = models.ManyToMany(Stock)
    quantity = models.IntegerField()
    cost_price = models.DecimalField(max_digits=20, decimal=2)
    amount = models.DecimalField(max_digits=20, decimal=2) # quantity * cost_price
