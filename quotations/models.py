from datetime import datetime

from django.db import models

from customers.models import Customer
from warehouses.models import Warehouse


class Quotation(models.Model):
    invoice_no = models.IntegerField() # Starts at 1
    date = models.DateField()
    warehouse = models.ForeignKey(Warehouse)
    customer = models.ForeignKey(Customer)
    remarks = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now())
    updated_at = models.DateTimeField(auto_now=True, default=datetime.now())

    def __unicode__(self):
        return u'%s' % self.invoice_no

    def info(self):
        return {
            'invoice_no': self.invoice_no,
            'date': self.date.isoformat(),
            'warehouse': self.warehouse.name,
            'customer': self.customer.__unicode__(),
            'remarks': self.remarks,
        }
