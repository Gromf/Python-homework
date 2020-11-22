"""
Задание 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который
должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""
'''
Матрицы должны иметь одинаковый размер. Должен передаваться список со списками пример:
[[x, y], [a, b]] и т д.
'''


class Matrix:

    def __init__(self, *args):
        self.matrix_element = args

    def __str__(self):
        for element in self.matrix_element[0]:
            for element_low in element:
                print(f'{element_low} ', end='')
            print()
        return f''

    def __add__(self, other: list):
        matrix = []

        if len(self.matrix_element[0]) != len(other.matrix_element[0]):
            return f'Матрицы имеют разный размер'
        for element in range(0, len(self.matrix_element[0])):
            matrix_low = []
            if len(self.matrix_element[0][element]) != len(other.matrix_element[0][element]):
                return f'Матрицы имеют разный размер'
            for element_low in range(0, len(self.matrix_element[0][element])):
                matrix_low.append(
                    self.matrix_element[0][element][element_low] + other.matrix_element[0][element][element_low]
                )
            matrix.append(matrix_low)
        return Matrix(matrix)


a = [31, 22, 5], [37, 42], [51, 86]
b = [51, 36, 0], [15, 10], [31, 50]
c = [51, 36], [15, 10], [31, 50]

matrix_one = Matrix(a)
matrix_two = Matrix(b)
matrix_three = Matrix(c)

print('Первая матрица:')
print(matrix_one)
print('Вторая матрица:')
print(matrix_two)

result_matrix = matrix_two + matrix_one
wrong_matrix = matrix_one + matrix_three
print('Сумма матриц')
print(result_matrix)
print('Результат сложения разных матриц')
print(wrong_matrix)
