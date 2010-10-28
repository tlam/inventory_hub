from decimal import Decimal

from django.db import models

from home.models import Home
from stocks.models import Stock


class StockCart(models.Model):
    description = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.description

    def add_item(self, item_code):
        msg = {'success': '', 'warning': ''}
        try:
            stock = Stock.objects.get(item_code=item_code)
            StockCartItem.objects.create(cart = self, stock=stock)
            msg['success'] = 'Stock Item added'
        except Stock.DoesNotExist:
            msg['warning'] = 'Stock Item Code "%s" does not exist' % item_code

        return msg

    def has_taxable_items(self):
        cart_items = self.stockcartitem_set.all()
        for item in cart_items:
            if not item.stock.exempt_flag:
                return True
        return False

    def update_items(self, post):
        cart_items = self.stockcartitem_set.all()
        for item in cart_items:
            quantity_key = 'stock-cart-item-quantity-%i' % item.pk
            discount_key = 'stock-cart-item-discount-%i' % item.pk
            tax_key = 'stock-cart-item-tax-%i' % item.pk
            item.quantity = post.get(quantity_key, 0)
            item.discount = post.get(discount_key, 0)
            item.tax = post.get(tax_key, 0)
            item.save()

        for item in cart_items:
            delete_key = 'stock-cart-item-delete-%i' % item.pk
            if post.get(delete_key, 0):
                item.delete()

    def sub_total(self):
        cart_items = self.stockcartitem_set.all()
        total_amount = 0
        for item in cart_items:
            total_amount += item.total()
        return total_amount

    def total(self):
        cart_items = self.stockcartitem_set.all()
        total_amount = 0
        for item in cart_items:
            total_amount += item.total_and_tax()
        return total_amount

    def tax_total(self):
        cart_items = self.stockcartitem_set.all()
        total_amount = 0
        for item in cart_items:
            total_amount += item.tax_amount()
        return total_amount


class StockCartItem(models.Model):
    cart = models.ForeignKey(StockCart)
    stock = models.ForeignKey('stocks.Stock')
    quantity = models.IntegerField(default=0, blank=True)
    discount = models.FloatField(default=0, blank=True)
    tax = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def tax_amount(self):
        return self.total() * self.tax * Decimal('0.01')

    def total(self):
        return self.quantity * self.stock.retail_price

    def total_and_tax(self):
        return self.total() * (100 + self.tax) * Decimal('0.01')

    def calculate_tax(self):
        if self.stock.exempt_flag:
            return Decimal('0.00')
        else:
            if self.tax:
                return self.tax
            else:
                try:
                    return Home.objects.get().tax.percent
                except Home.DoesNotExist:
                    return Decimal('0.00')
