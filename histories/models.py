from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


ACTION_CHOICES = (
  ('C', 'Create'),
  ('U', 'Update'),
  ('D', 'Delete'),
)


class History(models.Model):
    action_type = models.CharField(max_length=1, choices=ACTION_CHOICES)
    model_name = models.CharField(max_length=50)
    model_id = models.IntegerField()
    user = models.ForeignKey(User)
    past = models.CharField(max_length=255, blank=True)
    present = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now())

    @staticmethod
    def created_history(present, user):
        print 'created_history'

    @staticmethod
    def updated_history(past, present, user):
        past_data = past.info()
        present_data = present.info()
        if not past_data == present_data:
            History.objects.create(
                action_type='U',
                model_name=present.__class__.__name__,
                model_id=present.id,
                user=user,
                past=past_data,
                present=present_data,
            )
            print 'updated_history'

    @staticmethod
    def deleted_history(past, user):
        print 'deleted_history'
