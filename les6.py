# ex1 Guessing game
import random

guess = random.randint(1, 100)

user = input(f'Это число {guess}? ')
guess_range = range(1, 301)
count = 0
while user != '=':
    if user == '<':
        guess_range = range(guess_range[0], guess)
    else:
        guess_range = range(guess + 1, guess_range[-1] + 1)
    guess = guess_range[0] + int((guess_range[-1] - guess_range[0]) / 2)
    user = input(f'Это число {guess}? ')
    count += 1
else:
    print('Победа!!!')
    print(count)
