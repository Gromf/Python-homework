"""
Задача 5. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return f'({self.real + other.real}+{self.imaginary + other.imaginary}j)'

    def __mul__(self, other):
        return f'({self.real * other.real - self.imaginary * other.imaginary}+' \
               f'{self.imaginary * other.real + self.real * other.imaginary}j)'


a = ComplexNumber(5, 10)
b = ComplexNumber(7, 3)

d = complex(5, 10)
e = complex(7, 3)


print(f'Умножение через перегрузку {a * b}')
print(f'Умножение через встроенный тип {d * e}')

print(f'Сложение через перегрузку {a + b}')
print(f'Сложение через встроенный тип {d + e}')


