"""
Задача 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т

"""


class Road:
    _length: int
    _width: int

    def __init__(self):
        self._width = number_take('Введите ширину дороги в метрах >>> ')
        self._length = number_take('Введите длину дороги в метрах >>> ')

    def mass_calculation(self, mass_def=1, height=1):
        mass = self._width * self._length * mass_def * height / 1000  # /1000 перевод килограммов в тонны
        print(f'Необходимо {mass:.2f} тонн асфальта')


def number_take(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print('Необходимо число')
            continue


user_road = Road()
user_height = number_take('Введите высоту асфальтного слоя в сантиметрах >>> ')
user_mass_def = number_take('Введите массу одного квадратного метра асфальта толщиной 1 см в килограммах >>> ')
user_road.mass_calculation(user_mass_def, user_height)
