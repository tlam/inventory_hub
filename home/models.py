from django.db import models


class Home(models.Model):
    tax = models.ForeignKey('taxes.Tax')
