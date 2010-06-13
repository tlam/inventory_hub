from django.db import models

from communications.models import Phone
from geography.models import City, Country


class Supplier(models.Model):
    PRICE_CHOICES = (
        ('R', 'R'),
        ('W', 'W'),
        ('D', 'D'),
        ('S', 'S'),
    )

    supplier_no = models.CharField(max_length=100)  # CCCCCC-N, 
    company_name = models.CharField(max_length=100, blank=True)
    creditors_code = models.CharField(max_length=20, blank=True)  # Local creditors or Foreign creditors
    price_type = models.CharField(max_length=1, choices=PRICE_CHOICES)
    address = models.CharField(max_length=255, blank=True)
    city = models.ForeignKey(City)
    country = models.ForeignKey(Country)
    postal_code = models.CharField(max_length=6, blank=True)
    phone = models.ManyToManyField(Phone, null=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    vat_flag = models.BooleanField(default=False)
    vat_registration_number = models.IntegerField()  # 8 digit max
    business_registration_number = models.CharField(max_length=9)
