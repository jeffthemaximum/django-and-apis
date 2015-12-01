from django.db import models
from django.utils import timezone


class Image(models.Model):
    user = models.ForeignKey('auth.User')
    token = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
