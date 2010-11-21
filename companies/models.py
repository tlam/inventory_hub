from django.db import models

from contacts.models import ContactList


class Company(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=255)
    unit_number = models.CharField(max_length=50, blank=True, \
        verbose_name='House/Appt No')
    street = models.CharField(max_length=255, blank=True)
    town = models.ForeignKey('geography.Town', null=True, blank=True)
    country = models.ForeignKey('geography.Country', null=True, blank=True)
    vat_number = models.IntegerField(default=0, blank=True, \
        verbose_name='VAT Registration Number')
    business_number = models.CharField(max_length=20, blank=True, \
        verbose_name='Business Registration Number')
    vat_percentage = models.DecimalField(max_digits=4, decimal_places=2, \
        default=0, blank=True)
    logo = models.ImageField(upload_to='company_logos', blank=True, null=True)
    contact_list = models.ForeignKey(ContactList, blank=True, null=True)
   
    def __unicode__(self):
        return u'%s' % self.name

    def save(self, *args, **kwargs):
        if not self.contact_list:
            description = self.name
            self.contact_list = ContactList.objects.create(description=description[:10])    
        super(Company, self).save(*args, **kwargs)
