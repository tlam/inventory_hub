from django.db import models

from customers.models import Customer
from stocks.models import Warehouse


class Quotation(models.Model):
    invoice_no = models.IntegerField() # Starts at 1
    date = models.DateField()
    warehouse = models.ForeignKey(Warehouse)
    customer = models.ForeignKey(Customer)
    remarks = models.CharField(max_length=255)
    #clerk_name = # Fk to User
