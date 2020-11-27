"""
Задача 3.Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только
числами. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на
экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""


class NotNumber(Exception):
    def __init__(self, text):
        self.text = text


def number_check(number):
    try:
        if number.isdigit():
            return int(number)
        else:
            raise NotNumber('Введено не число')
    except NotNumber as err:
        print(err)
        return False


user_list = []

while True:
    user_input = input('Введите число или "Stop" >>> ')
    if user_input.lower() == 'stop':
        break
    if number_check(user_input):
        user_list.append(user_input)

print(user_list)
