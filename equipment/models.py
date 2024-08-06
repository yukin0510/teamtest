from django.db import models
from django.conf import settings

class Equipment(models.Model):
  class Meta:
    db_table = 'equip'

  equip_name = models.CharField(max_length=50,null=False)
  category = models.CharField(max_length=50,null=False)
  place = models.CharField(max_length=50,null=False)
  condition  = models.CharField(max_length=50,null=False)
  stock = models.PositiveIntegerField(null=False)
  text = models.TextField(null=False)
  image = models.ImageField(upload_to='images/', blank=False, null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)

