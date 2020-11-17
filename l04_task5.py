"""
Задача 5.
Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
"""

from functools import reduce


def multiplication(prev_el, el):
    return prev_el * el


number_list = [number for number in range(100, 1001) if number % 2 == 0]


print(reduce(multiplication, number_list))
