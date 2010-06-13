from django.db import models


class Phone(models.Model):
    PHONE_CHOICES = (
        (u'H', u'Home'),
        (u'W', u'Work'),
        (u'M', u'Mobile'),
        (u'HF', u'Home Fax'),
        (u'WF', u'Work Fax'),
        (u'O', u'Other'),
    )

    number = models.CharField(max_length=20)
    phone_type = models.CharField(max_length=2, choices=PHONE_CHOICES)
