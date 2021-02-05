import json
import pickle
import os

os.chdir(os.path.dirname(__file__))

with open('group.json', 'r') as f:
    my_favourite_group_js = json.load(f)


with open('group.pickle', 'rb') as f:
    my_favourite_group_pi = pickle.load(f)

print(my_favourite_group_js)
print(my_favourite_group_pi)