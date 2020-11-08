# Задача 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

# создаем список, сортируем его по убыванию и суммируем 2 первых элемента
def max_two_sum(number1, number2, number3):
    number_list = [number1, number2, number3]
    number_list.sort(reverse=True)
    return number_list[0] + number_list[1]


def number_check(user_number):
    while True:
        try:
            return int(user_number)
        except ValueError:
            user_number = input('Ошибка вводом, введите число >>> ')


user_number1 = number_check(input('Введите первое число >>> '))
user_number2 = number_check(input('Введите второе число >>> '))
user_number3 = number_check(input('Введите третье число >>> '))

print(max_two_sum(user_number1, user_number2, user_number3))
