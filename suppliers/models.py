from django.db import models

class Supplier(models.Model):
    supplier_no = models.CharField(max=) # CCCCCC-N, 
    company_name = models.CharField(max=100, null=True, blank=True)
    creditors_code = # Local creditors or Foreign creditors
    price_type = # R, W, D, S
    address = models.CharField(max=255)
    city = models.ForeignKey(City)
    country = models.ForeignKey(Country)
    postal_code = models.CharField(max=6)
    phone = models.ManyToManyField(Phone)
    first_name = models.CharField(max=50, null=True, blank=True)
    last_name = models.CharField(max=100, null=True, blank=True)
    vat_flag = # Y or N  , Optional
    vat_registration_number = models.IntegerField() # 8 digit max
    business_registration_number = models.CharField(max=9)
