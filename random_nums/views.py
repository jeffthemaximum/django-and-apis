from __future__ import division
from django.shortcuts import render
from django.db.models import F
from .models import Random_Num
from ip.helpers import ApiGet


def get_random_num_from_api(request):
    #get ip address details
    random_call = ApiGet("https://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint8", request)
    random_num = random_call.get_json_response()["data"][0]
    print str(random_num)
    return random_num


def get_total_rows():
    # get total rows in Random_Num
    return Random_Num.objects.count()


def update_each_row_with_total_count(count):
    Random_Num.objects.all().update(total_count=count)


def update_frequency_on_all_rows(total_rows):
    # this might work, not sure
    all_random_nums = Random_Num.objects.all()
    for num in all_random_nums:
        num.frequency = num.count / total_rows
        num.save()


def update_frequency():
    # get total rows in Random_Num
    # update all records with count/frequency
    # something like
    total_rows = get_total_rows()
    # update each row with total_count
    # update_each_row_with_total_count(total_rows)
    # update frequency column on every row
    update_frequency_on_all_rows(total_rows)
    return total_rows


def update_random_num(random_num):
    # update count
    number = Random_Num.objects.get(number=random_num)
    number.count += 1
    number.save()
    total_rows = update_frequency()
    return [number, total_rows]


def create_new_num(random_num):
    total_rows = get_total_rows() + 1
    frequency = 1 / total_rows
    number = Random_Num(number=random_num, frequency=frequency)
    number.save()
    return [number, total_rows]


def get_all_random_nums():
    return Random_Num.objects.order_by("-count", "number")


def random_index(request):
    random_num = get_random_num_from_api(request)
    exists = Random_Num.objects.filter(number=random_num).exists()
    # save to db if doesn't exist
    if exists is True:
        num_data = update_random_num(random_num)
    else:
        num_data = create_new_num(random_num)
    total_rows = num_data[1]
    number = num_data[0]
    update_frequency_on_all_rows(total_rows)
    all_nums = get_all_random_nums()
    return render(request, 'random_nums/random_index.html', {'random_num': number, 'all_nums': all_nums})
