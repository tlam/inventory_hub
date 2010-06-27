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
    #clerk_name = # Fk to User

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s' % self.customer

class CashSale(Sale):
    pass

class CreditSale(Sale):
    pass

