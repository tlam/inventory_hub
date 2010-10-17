from django.db import models

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

    def update_items(self, post):
        cart_items = self.stockcartitem_set.all()
        for item in cart_items:
            quantity_key = 'stock-cart-item-quantity-%i' % item.pk
            discount_key = 'stock-cart-item-discount-%i' % item.pk
            item.quantity = post.get(quantity_key, 0)
            item.discount = post.get(discount_key, 0)
            item.save()

        for item in cart_items:
            delete_key = 'stock-cart-item-delete-%i' % item.pk
            if post.get(delete_key, 0):
                item.delete()


class StockCartItem(models.Model):
    cart = models.ForeignKey(StockCart)
    stock = models.ForeignKey('stocks.Stock')
    quantity = models.IntegerField(default=0, blank=True)
    discount = models.FloatField(default=0, blank=True)

    def total(self):
        return self.quantity * self.stock.retail_price
