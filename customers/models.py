from django.db import models

class City(models.Model):
    name = models.CharField(max=100)

class Country(models.Model):
    name = models.CharField(max=100)

class Phone(models.Model):
    number = models.CharField(max=12)
    type = # home, work, mobile, home fax, work fax, skype_name

class Customer(models.Model):
    cutomer_no = models.CharField(max=) # LLL-FFF-N, 
    first_name = models.CharField(max=50, null=True, blank=True)
    last_name = models.CharField(max=100, null=True, blank=True)
    company_name = models.CharField(max=100, null=True, blank=True)
    price_type = # R, W, D, S
    address = models.CharField(max=255)
    city = models.ForeignKey(City)
    country = models.ForeignKey(Country)
    phone = models.ManyToManyField(Phone)
    email = models.CharField(max=100)
    vat_flag = # Y or N  , Optional
    vat_registration_number = models.IntegerField() # 8 digit max
    business_registration_number = models.CharField(max=9)
    discount_percent = models.FloatField()
