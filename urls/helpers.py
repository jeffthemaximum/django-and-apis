# from .models import Url
import random
import pudb

def random_lowercase():
    return chr(random.randint(97, 122))

def random_uppercase():
    return chr(random.randint(65, 90))

def generate_key():
    key = []

    # add 8 letters or numbers to key
    for i in range(8):
        # determine if I should add number or letter
        decider = random.random()

        # 1/3 of the time, add a number between 0 and 9, inclusive
        if decider < (1/float(3)):
            adder = str(random.randint(0, 9))

        # 1/3 of time, add a lowercase letter
        elif decider < (2/float(3)):
            adder = random_lowercase()

        # 1/3 of the time, add uppercase letter
        else:
            adder = random_uppercase()

        # append adder to key
        key.append(adder)

    return ("".join(key))

# def key_exists(key):
#     return Url.objects.filter(key=key) != []