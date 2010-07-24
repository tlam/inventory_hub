from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from customers.models import Customer
from quotations.models import Quotation
from stocks.models import Stock, Warehouse


class Sale(models.Model):
    invoice_no = models.IntegerField() # CHN starts at N=1
    date = models.DateField()
    #quotation = models.ForeignKey(Quotation)
    warehouse = models.ForeignKey(Warehouse)
    customer = models.ForeignKey(Customer)
    remarks = models.CharField(max_length=255, blank=True)
    recquisition_number = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now())
    updated_at = models.DateTimeField(auto_now=True, default=datetime.now())

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s' % self.customer

    def info(self):
        return {
            'invoice_no': self.invoice_no,
            'date': self.date.isoformat(),
            'warehouse': self.warehouse.__unicode__(),
            'customer': self.customer.__unicode__(),
            'remarks': self.remarks,
            'recquisition_number': self.recquisition_number,
        }

class CashSale(Sale):
    pass

class CreditSale(Sale):
    pass
