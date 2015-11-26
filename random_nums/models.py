from __future__ import division
from django.db import models
from django.utils import timezone


class Random_Num(models.Model):
    number = models.IntegerField()
    count = models.IntegerField(default=0)
    total_count = models.IntegerField(default=0)
    frequency = models.DecimalField(max_digits=11, decimal_places=10)

    def update_frequency(self):
        self.frequency = self.count / self.total_count

    def __str__(self):
        return self.number
