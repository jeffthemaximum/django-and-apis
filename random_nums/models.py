from __future__ import division
from django.db import models
from django.utils import timezone


class Random_Num(models.Model):
    number = models.IntegerField()
    count = models.IntegerField(default=1)
    total_count = models.IntegerField(default=0)
    frequency = models.DecimalField(max_digits=11, decimal_places=10)

    def update_frequency_count(self, total_count):
        self.frequency = self.count / total_count
        self.save()

    def __str__(self):
        return str(self.number)
