from __future__ import division
from django.shortcuts import render
from .models import Random_Num


def get_total_rows():
    # get total rows in Random_Num
    return Random_Num.objects.count()


def update_each_row_with_total_count(count):
    Random_Num.objects.all().update(total_count=count)


def update_frequency_on_all_rows(total_rows):
    # this might work, not sure
    Random_Num.objects.all().update(frequency= (F('count') / F('total_rows'))


def update_frequency():
    # get total rows in Random_Num
    # update all records with count/frequency
    # something like
    total_rows = get_total_rows()
    # update each row with total_count
    update_each_row_with_total_count(total_rows)
    # update frequency column on every row
    update_frequency_on_all_rows(total_rows)

