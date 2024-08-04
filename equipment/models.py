from django.db import models
from django.utils import timezone 

class Equipment(models.Model):
  class Meta:
    db_table = 'equip'

  equip_name = models.CharField()
  category = models.CharField()
  place = models.CharField()
  condition  = models.CharField()
  stock = models.PositiveIntegerField()
  detail = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)