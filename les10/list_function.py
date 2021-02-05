import random


def random_item(input_list):
    if input_list:
        rand_item = random.choice(input_list)
        return rand_item

