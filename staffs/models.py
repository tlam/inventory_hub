from django.db import models


class SalesAgent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['first_name']

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

