from django.db import models
from django.utils import timezone 

class Equipment(models.Model):
  class Meta:
    db_table = 'equip'

  equip_name = models.CharField(max_length=50)
  category = models.CharField(max_length=50)
  place = models.CharField(max_length=50)
  condition  = models.CharField(max_length=50)
  stock = models.PositiveIntegerField()
  text = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(default=timezone.now)