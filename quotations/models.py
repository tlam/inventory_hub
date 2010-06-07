from django.db import models

class Quotation(models.Model):
    invoice_no = models.IntegerField() # Starts at 1
    date = models.DateField()
    warehouse = models.ForeignKey(Warehouse)
    customer = models.ForeignKey(Customer)
    remarks = models.CharField(max=255)
    stocks = models.ManyToMany(Stock)
    quantity = models.IntegerField()
    discount = models.FloatField()
    clerk_name = # Fk to User
