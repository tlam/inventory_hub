from django.db import models

class CashSale(models.Model):
    invoice_no = models.IntegerField() # CHN starts at N=1
    date = models.DateField()
    quotation = models.ForeignKey(Quotation)
    warehouse = models.ForeignKey(Warehouse)
    customer = models.ForeignKey(Customer)
    remarks = models.CharField(max=255)
    recquisition_number = models.CharField(max=255)
    stocks = models.ManyToMany(Stock)
    quantity = models.IntegerField()
    discount = models.FloatField()
    clerk_name = # Fk to User

class CreditSale(models.Model):
    invoice_no = models.IntegerField() # CRN starts at N=1
    date = models.DateField()
    quotation = models.ForeignKey(Quotation)
    warehouse = models.ForeignKey(Warehouse)
    customer = models.ForeignKey(Customer)
    remarks = models.CharField(max=255)
    recquisition_number = models.CharField(max=255)
    stocks = models.ManyToMany(Stock)
    quantity = models.IntegerField()
    discount = models.FloatField()
    clerk_name = # Fk to User
