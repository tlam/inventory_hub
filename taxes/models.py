from django.db import models


class Tax(models.Model):
    name = models.CharField(max_length=6)
    percent = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __unicode__(self):
        return u'%s' % self.name
