from django.db import models

from django.utils import timezone


class Ip(models.Model):
    user = models.ForeignKey('auth.User')
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    isp_provider = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    date_used = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.address
