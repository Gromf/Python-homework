"""
Задача 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на
данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""


class DivisionZero(Exception):
    def __init__(self, text):
        self.text = text


def division(dividend, divider):
    try:
        if divider == 0:
            raise DivisionZero('Деление на 0')
        return round(dividend / divider, 2)
    except DivisionZero as error:
        return error


def number_take(text: str):
    while True:
        try:
            number = float(input(text))
            return number
        except ValueError:
            print('Введите число')


user_dividend = number_take('Введите делимое >>> ')
user_divider = number_take('Введите делитель >>> ')

print(division(user_dividend, user_divider))
