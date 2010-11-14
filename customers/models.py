from datetime import datetime

from django.db import models
from django.db.models.signals import post_save

from contacts.models import ContactList
from geography.models import City, Country
from utils.constants import PRICE_CHOICES

now = datetime.now()


class Customer(models.Model):
    customer_no = models.CharField(max_length=100)  # LLL-FFF-N
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True)
    price_type = models.CharField(max_length=2, choices=PRICE_CHOICES)
    unit_number = models.CharField(max_length=50, blank=True, \
        verbose_name='House/Appt No')
    street = models.CharField(max_length=255, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True)
    vat_registration_number = models.IntegerField(default=0, blank=True)
    business_registration_number = models.CharField(max_length=9, blank=True)
    discount_percent = models.FloatField(default=0, blank=True)
    contact_list = models.ForeignKey(ContactList, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, default=now)
    updated_at = models.DateTimeField(auto_now=True, default=now)

    class Meta:
        unique_together = (('first_name', 'last_name'),)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        if not self.contact_list:
            description = self.customer_no
            self.contact_list = ContactList.objects.create(description=description[:10])    
        super(Customer, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('customers:update', [self.id])

    def info(self):
        if self.city:
            city = self.city.name
        else:
            city = ''

        if self.country:
            country = self.country.name
        else:
            country = ''

        return {
            'customer_no': self.customer_no,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'company_name': self.company_name,
            'price_type': self.price_type,
            'street': self.street,
            'city': city,
            'country': country,
            'vat_registration_number': self.vat_registration_number,
            'business_registration_number': self.business_registration_number,
            'discount_percent': self.discount_percent,
        }
