from django.db import models

from communications.models import Phone
from geography.models import City, Country
from utils.constants import PRICE_CHOICES

class Customer(models.Model):
    cutomer_no = models.CharField(max_length=100, blank=True)  # LLL-FFF-N, 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True)
    price_type = models.CharField(max_length=2, choices=PRICE_CHOICES)
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City)
    country = models.ForeignKey(Country)
    phone = models.ManyToManyField(Phone)
    email = models.CharField(max_length=100)
    vat_flag = models.BooleanField(default=False)
    vat_registration_number = models.IntegerField()  # 8 digit max
    business_registration_number = models.CharField(max_length=9)
    discount_percent = models.FloatField()
