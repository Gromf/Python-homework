"""
Задача 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте
в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""


class Car:
    speed: int
    color: str
    name: str
    is_police = False  # по умолчанию определяем для класса Car, при инициализации не передаем этот параметр

    def __init__(self, name, color, speed):
        self.speed, self.color, self.name = speed, color, name

    def go(self):
        print('Машина едет')

    def stop(self):
        print('Машина стоит')

    def turn(self, direction):
        if direction == 'left':
            print(f'{self.name} поварачивает налево')
        elif direction == 'right':
            print(f'{self.name} поварачивает направо')
        elif direction == 'forward':
            print(f'{self.name} едет прямо')
        elif direction == 'back':
            print(f'{self.name} поварачивает назад')
        else:
            print(f'{self.name} в панике')

    def show_speed(self):
        print(f'Скорость машины {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость выше разрешенной! Сейчас скорость {self.speed}')
        else:
            print(f'Скорость машины {self.speed}')


class SportCar(Car):

    def __init__(self, name, color, speed):
        super(SportCar, self).__init__(name, color, speed)
        if color.lower() == 'red' or color.lower() == 'красный':
            self.color = 'Red iz da fasta!!!'
        else:
            self.color = color


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость выше разрешенной! Сейчас скорость {self.speed}')
        else:
            print(f'Скорость машины {self.speed}')


class PoliceCar(Car):
    is_police = True  # определяем для дочернего класса PoliceCar и не передаем


fast_car = SportCar('Феррари', 'Красный', 200)
slow_car = TownCar('Ниссан', 'Черный', 79)
strong_car = WorkCar('Пикап', 'Коричневый', 120)
law_car = PoliceCar('Порш', 'Белый', 0)

print('Значения для SportCar:')
print(f'Название {fast_car.name}, цвет {fast_car.color}, Скорость {fast_car.speed}, полиция? {fast_car.is_police}')
fast_car.show_speed()
fast_car.turn('left')
fast_car.go()

print('\nЗначения для PoliceCar:')
print(f'Название {law_car.name}, цвет {law_car.color}, Скорость {law_car.speed}, полиция? {law_car.is_police}')
law_car.show_speed()
law_car.turn('')
law_car.stop()

print('\nЗначения для WorkCar:')
print(f'Название {strong_car.name}, цвет {strong_car.color}, Скорость {strong_car.speed}, полиция?'
      f' {strong_car.is_police}')
strong_car.show_speed()
strong_car.turn('forward')

print('\nЗначения для TownCar:')
print(f'Название {slow_car.name}, цвет {slow_car.color}, Скорость {slow_car.speed}, полиция? {slow_car.is_police}')
slow_car.show_speed()
slow_car.turn('back')
