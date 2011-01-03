from datetime import datetime

from django.db import models
from django.db.models.signals import post_save

from contacts.models import ContactList
from customers.models import Customer
from sales.models import CashSale, CreditSale
from stock_carts.models import StockCart
from warehouses.models import Warehouse


class Quotation(models.Model):
    invoice_no = models.IntegerField() # Starts at 1
    date = models.DateField()
    sales_agent = models.ForeignKey('staffs.SalesAgent', blank=True, null=True)
    warehouse = models.ForeignKey(Warehouse)
    customer = models.ForeignKey(Customer)
    remarks = models.CharField(max_length=255, blank=True)
    cart = models.ForeignKey('stock_carts.StockCart', blank=True, null=True)
    contact_list = models.ForeignKey(ContactList, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now())
    updated_at = models.DateTimeField(auto_now=True, default=datetime.now())

    def __unicode__(self):
        return u'%s' % self.invoice_no

    def save(self, *args, **kwargs):
        if not self.contact_list:
            description = 'Quotation:%i' % self.invoice_no
            self.contact_list = ContactList.objects.create(description=description[:10])
        super(Quotation, self).save(*args, **kwargs)

    def info(self):
        return {
            'invoice_no': self.invoice_no,
            'date': self.date.isoformat(),
            'warehouse': self.warehouse.name,
            'customer': self.customer.__unicode__(),
            'remarks': self.remarks,
        }

    def to_cash_sale(self):
        return CashSale.objects.create(
            invoice_no=self.invoice_no,
            date=self.date,
            warehouse=self.warehouse,
            customer=self.customer,
            remarks=self.remarks,
            cart=self.cart,
            contact_list=self.contact_list
        )

    def to_credit_sale(self):
        return CreditSale.objects.create(
            invoice_no=self.invoice_no,
            date=self.date,
            warehouse=self.warehouse,
            customer=self.customer,
            remarks=self.remarks,
            cart=self.cart,
            contact_list=self.contact_list
        )


#@receiver(pre_init, sender=Quotation), IN FUTURE DJANGO RELEASE
def create_cart(sender, **kwargs):
    quotation = kwargs['instance']
    if not quotation.cart:
        description = 'Q-%i' % quotation.invoice_no
        quotation.cart = StockCart.objects.create(description=description[:10])
        quotation.save()

post_save.connect(create_cart, sender=Quotation)
