import pickle
import json
import os

os.chdir(os.path.dirname(__file__))


my_favourite_group = {
    'name': 'Hi-Fi',
    'tracks': ['Седьмой лепесток', 'Беспризорник'],
    'Albums': [{'name': 'The Best', 'year': 2000},
               {'name': 'Пионер', 'year': 2011}]}

with open('group.json', 'w') as f:
    json.dump(my_favourite_group, f)

print('JSon Объект записан')

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)

print('Pickle Объект записан')