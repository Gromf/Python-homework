"""
Задача 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только
первые n чисел, начиная с 1! и до n!.
"""

# не очень понял условия, можно передавать в функцию последнее число факториала или она должна работать до бесконечности
# реализовал оба варианта. Использовать factorial(N) из модуля math в этой задаче считаю не корректным

from itertools import count


# функция с передачей числа для которого рассчитывается факториал
def factorial(number=0):
    if number == 0:  # для определения 0!
        yield 1
    else:
        fact = 1
        for el in range(1, number + 1):
            fact = fact * el
            yield fact


# функция с расчетом до бесконечности
def factorial_infinity(number=0):
    if number == 0:  # для определения 0!
        yield 1
    else:
        fact = 1
        for el in count(1):
            fact = fact * el
            yield fact


def number_check(user_number):
    while True:
        try:
            return int(user_number)
        except ValueError:
            user_number = input('Введите число >>> ')


user_factorial = abs(number_check(input('Введите число факториала >>> ')))


# блок для вывода результата под функцию с бесконечностью.
print('Используя функцию с расчетом до бесконечности')
if user_factorial == 0:
    factorial_number = 0  # для определения 0!
else:
    factorial_number = 1

for fact_number in factorial_infinity(user_factorial):
    print(f'Факториал {factorial_number}! = {fact_number}')
    factorial_number += 1
    if factorial_number > user_factorial:
        break

# блок вызова функции с передачей числа
print('Используя функцию с расчетом до заданного числа')
if user_factorial == 0:
    factorial_number = 0  # для определения 0!
else:
    factorial_number = 1

for fact_number in factorial(user_factorial):
    print(f'Факториал {factorial_number}! = {fact_number}')
    factorial_number += 1
