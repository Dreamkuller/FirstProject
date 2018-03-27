import random

dishes_string = input('What would you like? ')
b = list(set(dishes_string.split(', ')))

for n in range(0, len(b)):
    print(b[n], (20 - len(b[n])) * '.', random.randrange(1, 60, 1), 'min')
