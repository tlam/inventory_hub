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
