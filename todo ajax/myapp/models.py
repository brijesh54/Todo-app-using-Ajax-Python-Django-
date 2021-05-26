
from django.db import models

class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)
    priority = models.IntegerField(blank=True, null=True)