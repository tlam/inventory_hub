from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

class Warehouse(models.Model):
    name = models.CharField(max_length=100, default='')

    def __unicode__(self):
        return self.name

class Price(models.Model):
    retail_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    #measure = # sq ft, mm, unit

class Stock(models.Model):
    item_code = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=255, default='')
    category = models.ForeignKey(Category)
    retail_price = models.ForeignKey(Price, related_name='retail')
    wholesale_price = models.ForeignKey(Price, related_name='wholesale')
    dealer_price = models.ForeignKey(Price, related_name='dealer')
    special_price = models.ForeignKey(Price, related_name='special')
    pieces_per_box = models.IntegerField(null=True, blank=True, default=0)
    exempt_flag = models.BooleanField(default=False)
    nonstock_flag = models.BooleanField(default=False)
'''
    # country
    # supplier
'''
