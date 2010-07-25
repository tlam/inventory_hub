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
    past = models.TextField(blank=True)
    present = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now())

    class Meta:
        verbose_name_plural = 'Histories'

    @staticmethod
    def created_history(present, user):
        print 'created_history'
        History.objects.create(
            action_type='C',
            model_name=present.__class__.__name__,
            model_id=present.id,
            user=user,
            present=present.info(),
        )

    @staticmethod
    def updated_history(past, present, user):
        if isinstance(past, models.query.QuerySet):
            past_data = {}
            present_data = {}
            for item in past:
                past_data[item.id] = item.info()
            present_data = {}
            for item in present:
                present_data[item.id] = item.info()

            if not past_data and present_data:
                action_type = 'C'
            elif past_data and present_data:
                action_type = 'U'
            else:
                action_type = 'D'

            if not past_data == present_data:
                History.objects.create(
                    action_type=action_type,
                    model_name='StockItem',
                    model_id=0,
                    user=user,
                    past=past_data,
                    present=present_data,
                )
        else:
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

    @staticmethod
    def deleted_history(past, user):
        print 'deleted_history'
