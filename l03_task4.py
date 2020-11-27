# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# возведение в отрицательную степень через цикл
def exponentiation(number1, number2):
    number = 1
    for count in range(0, number2, -1):
        number *= number1
    return 1 / number


# возведение в отрицательную степень через оператор **
def exponentiation_easy(number1, number2):
    return number1 ** number2


while True:
    base_degree = input('Введите положительное основание >>> ')
    try:
        base_degree = float(base_degree)
        if base_degree > 0:
            break
        print('Ошибка ввода')
    except ValueError:
        print('Ошибка ввода')

while True:
    exponent = input('Введите отрицательное целое число показателя степени >>> ')
    try:
        exponent = int(exponent)
        if exponent < 0:
            break
        print('Ошибка ввода')
    except ValueError:
        print('Ошибка ввода')

print(f'{base_degree} в степени {exponent} через цикл = {exponentiation(base_degree, exponent)}')
print(f'{base_degree} в степени {exponent} через ** = {exponentiation_easy(base_degree, exponent)}')
