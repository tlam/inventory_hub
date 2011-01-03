from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from contacts.models import ContactList
from customers.models import Customer
from warehouses.models import Warehouse

class Sale(models.Model):
    invoice_no = models.IntegerField() # CHN starts at N=1
    date = models.DateField()
    sales_agent = models.ForeignKey('staffs.SalesAgent', blank=True, null=True)
    warehouse = models.ForeignKey(Warehouse)
    customer = models.ForeignKey(Customer)
    remarks = models.CharField(max_length=255, blank=True)
    requisition_number = models.CharField(max_length=255, blank=True)
    cart = models.ForeignKey('stock_carts.StockCart', blank=True, null=True)
    contact_list = models.ForeignKey('contacts.ContactList', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now())
    updated_at = models.DateTimeField(auto_now=True, default=datetime.now())

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s' % self.customer

    def save(self, *args, **kwargs):
        if not self.contact_list:
            description = 'Sale:%i' % self.invoice_no
            self.contact_list = ContactList.objects.create(description=description[:10])
        super(Sale, self).save(*args, **kwargs)

    def info(self):
        return {
            'invoice_no': self.invoice_no,
            'date': self.date.isoformat(),
            'warehouse': self.warehouse.__unicode__(),
            'customer': self.customer.__unicode__(),
            'remarks': self.remarks,
            'requisition_number': self.requisition_number,
        }

class CashSale(Sale):
    pass

class CreditSale(Sale):
    pass


def create_cart(sender, **kwargs):
    from stock_carts.models import StockCart
    sale = kwargs['instance']
    if not sale.cart:
        description = 'S-%i' % sale.invoice_no
        sale.cart = StockCart.objects.create(description=description[:10])
        sale.save()

post_save.connect(create_cart, sender=CashSale)
post_save.connect(create_cart, sender=CreditSale)
