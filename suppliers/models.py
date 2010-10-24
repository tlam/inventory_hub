from django.db import models

from geography.models import City, Country
from utils.constants import PRICE_CHOICES


class BaseSupplier(models.Model):
    supplier_no = models.CharField(max_length=100, unique=True)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True)
    city = models.ForeignKey(City)
    country = models.ForeignKey(Country)
    postal_code = models.CharField(max_length=6, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s' % self.company_name

    def info(self):
        return {
            'supplier_no': self.supplier_no,
            'company_name': self.company_name,
            'address': self.address,
            'city': self.city.name,
            'country': self.country.name,
            'postal_code': self.postal_code,
            'phone': self.phone,
            'first_name': self.first_name,
            'last_name': self.last_name,
        }


class LocalSupplier(BaseSupplier):
    creditors_code = models.CharField(max_length=20, blank=True)  # Local creditors or Foreign creditors
    price_type = models.CharField(max_length=1, choices=PRICE_CHOICES)
    town = models.ForeignKey('geography.Town', blank=True, null=True)
    vat_flag = models.BooleanField(default=False)
    vat_registration_number = models.IntegerField(default=0, blank=True)  # 8 digit max
    business_registration_number = models.CharField(max_length=9, blank=True)

    def info(self):
        local_info = {
            'vat_flag': self.vat_flag,
            'vat_registration_number': self.vat_registration_number,
            'business_registration_number': self.business_registration_number,
        }
        base_info = super(self.__class__, self).info()
        base_info.update(local_info)
        return base_info


class ForeignSupplier(BaseSupplier):
    pass


class SupplierFactory:
    @staticmethod
    def create(supplier_type):
        if supplier_type == 'foreign':
            return ForeignSupplier
        else:
            return LocalSupplier
