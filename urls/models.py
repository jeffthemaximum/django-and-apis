from django.db import models
from .helpers import *
import random


# Create your models here.
class Url(models.Model):
    user = models.ForeignKey('auth.User', null=True)
    long_url = models.URLField(max_length=500)
    key = models.CharField(max_length=8)

    def __str__(self):
        return self.long_url

    def make_key(self):
        self.key = generate_key()
        return self.key
