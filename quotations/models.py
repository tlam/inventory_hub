from datetime import datetime

from django.db import models
from django.db.models.signals import post_save

from customers.models import Customer
from stock_carts.models import StockCart
from warehouses.models import Warehouse


class Quotation(models.Model):
    invoice_no = models.IntegerField() # Starts at 1
    date = models.DateField()
    warehouse = models.ForeignKey(Warehouse)
    customer = models.ForeignKey(Customer)
    remarks = models.CharField(max_length=255, blank=True)
    cart = models.ForeignKey('stock_carts.StockCart', blank=True, null=True)
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


#@receiver(pre_init, sender=Quotation), IN FUTURE DJANGO RELEASE
def create_cart(sender, **kwargs):
    quotation = kwargs['instance']
    if not quotation.cart:
        description = 'Q-%i' % quotation.invoice_no
        quotation.cart = StockCart.objects.create(description=description[:10])
        quotation.save()

post_save.connect(create_cart, sender=Quotation)
