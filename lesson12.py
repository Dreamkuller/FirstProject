import random

dishes_string = input('What would you like? ')
b = list(set(dishes_string.split(', ')))


def preparing_time():
    return random.randrange(1, 60, 1)


for n in range(0, len(b)):
    print(b[n], (20 - len(b[n])) * '.', preparing_time(), 'min')


