# Задача 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        print('Деление на ноль')
        exit()


def number_check(user_number):
    while True:
        try:
            return float(user_number)
        except ValueError:
            user_number = input('Ошибка ввода, введите число >>> ')


dividend = number_check(input('Введите делимое >>> '))
divider = number_check(input('Введите делитель >>> '))

print(f'{division(dividend, divider):.2f}')
