from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Warehouse(models.Model):
    name = models.CharField(max_length=100, default='')

    def __unicode__(self):
        return self.name

class Price(models.Model):
    retail_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    #measure = # sq ft, mm, unit

'''
class Stock(models.Model):
    item_code = models.CharField(max=50)
    description = models.CharField(max=255)
    category = models.ForeignKey(Category)
    retail_price = models.ForeignKey(Price)
    wholesale_price = models.ForeignKey(Price)
    dealer_price = models.ForeignKey(Price)
    special_price = models.ForeignKey(Price)
    pieces_per_box = models.IntegerField(null=True, blank=True)
    exempt_flag = models  # Y or N
    nonstock_flag = models  # Y or N
    # country
    # supplier
'''
