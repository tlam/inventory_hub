from django.db import models

from customers.models import Customer


class Email(models.Model):
    EMAIL_CHOICES = (
        (u'H', u'Home'),
        (u'W', u'Work'),
    )
    customer = models.ForeignKey(Customer, related_name='customer_email')
    address = models.EmailField()
    email_type = models.CharField(max_length=1, choices=EMAIL_CHOICES)


class Phone(models.Model):
    PHONE_CHOICES = (
        (u'H', u'Home'),
        (u'HF', u'Home Fax'),
        (u'W', u'Work'),
        (u'WF', u'Work Fax'),
        (u'C', u'Cellphone'),
    )
    customer = models.ForeignKey(Customer)
    number = models.CharField(max_length=50)
    phone_type = models.CharField(max_length=2, choices=PHONE_CHOICES)
