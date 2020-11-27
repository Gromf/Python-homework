"""
Задача 6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""

from itertools import count
from itertools import cycle


def number_input(text):
    user_number = input(text)
    while True:
        try:
            return int(user_number)
        except ValueError:
            user_number = input(text)


number_count_start = number_input('Введите число для начала списка чисел >>> ')
quantity = abs(number_input('Введите количество чисел >>> '))


count_limit = 0
for number in count(number_count_start):
    print(number)
    count_limit += 1
    if count_limit == quantity:
        break


user_list = []
# в данном случае можно было ввести список по умолчанию, но пусть будет пользовательский
while True:
    user_list = input('Введите элементы списка через пробел >>> ').split()
    if len(user_list) > 0:
        break
    print('Вы не ввели список')

quantity = abs(number_input('Введите повторений элементов списка >>> '))


count_limit = 0
for word in cycle(user_list):
    print(word)
    count_limit += 1
    if count_limit == quantity:
        break


