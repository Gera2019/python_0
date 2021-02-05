# ex1
def friends(name, age, city):
    return f'{name}, {age} год(а), проживает в городе {city}'


print(friends('Аня', '34', 'Барнаул'))


# ex2
def max_number(numbers):
    return max(numbers)


print(max_number((8, 6, 67)))

# ex3
player1 = {'name': input('Введите ваше имя '), 'health': 100, 'damage': 10, 'armor': 1.2}
player2 = {'name': input('Введите ваше имя '), 'health': 100, 'damage': 10, 'armor': 1.5}


def attack(player, enemy):
    player['health'] -= enemy['damage']/player['armor']
    player['health'] = round(player['health'], 2)


print(f'{player2["name"]} attacks {player1["name"]}')
attack(player1, player2)
print(f'{player1["name"]} has {player1["health"]} of health after attack')
print(f'{player1["name"]} attacks {player2["name"]}')
attack(player2, player1)
print(f'{player2["name"]} has {player2["health"]} of health after attack')