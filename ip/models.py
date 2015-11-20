from django.db import models

from django.utils import timezone


class Ip(models.Model):
    user = models.ForeignKey('auth.User')
    address = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    date_used = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.address
