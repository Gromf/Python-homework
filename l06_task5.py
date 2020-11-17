"""
Задача 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра.
"""


class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Рисуем ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем карандашом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем маркером {self.title}')


user_pen = Pen('Паркер')
user_pencil = Pencil('твердомягким')
user_handle = Handle('зеленым')
user_stationery = Stationery('Принадлежность')

user_stationery.draw()
user_pen.draw()
user_pencil.draw()
user_handle.draw()
