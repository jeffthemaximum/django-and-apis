from django.db import models
from .helpers import *
import random


# Create your models here.
class Url(models.Model):
    user = models.ForeignKey('auth.User', null=True)
    long_url = models.URLField(max_length=500)
    key = models.CharField(max_length=8)
    hits = models.IntegerField(default=0)

    def __str__(self):
        return self.long_url

    def make_key(self):
        self.key = generate_key()
        self.save()
        return self.key

    def add_hit(self):
        self.hits += 1
        self.save()
