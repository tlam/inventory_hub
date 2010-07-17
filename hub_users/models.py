from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class HubUser(models.Model):
    user = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return u'%s' % self.user.username


def create_hub_user(sender, instance, **kwargs):
    HubUser.objects.get_or_create(user=instance)

post_save.connect(create_hub_user, sender=User)
