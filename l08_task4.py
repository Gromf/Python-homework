"""
Задача 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class Error(Exception):
    def __init__(self, text):
        self.text = text


class Check:

    @staticmethod
    def number_take(text):
        while True:
            try:
                number = int(input(text))
                if number <= 0:
                    raise Error('Введите положительное число число')
                return number
            except ValueError:
                print('Введите положительное число число')
            except Error as err:
                print(err)


class OfficeEquipment:
    name: str

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Printer(OfficeEquipment):
    color: bool

    def __init__(self, name, color=False):
        super(Printer, self).__init__(name)
        self.color = color


class Scanner(OfficeEquipment):
    public: bool

    def __init__(self, name, public=False):
        super(Scanner, self).__init__(name)
        self.public = public


class Copier(OfficeEquipment):
    pages_per_minute: int

    def __init__(self, name, pages_per_minute=10):
        super(Copier, self).__init__(name)
        self.pages_per_minute = pages_per_minute


class Storage:
    in_storage: dict

    def __init__(self):
        self.in_storage = {}

    def __str__(self):
        return f'На складе сейчас: {self.in_storage}'

    def take_to_storage(self, equipment, count):
        if equipment in self.in_storage.keys():
            self.in_storage[equipment] += count
        else:
            self.in_storage[equipment] = count
        print(f'На склад помещено {equipment} в количестве {count} шт., всего на складе '
              f'{self.in_storage.get(equipment)}')

    def take_from_storage(self, equipment, count):
        if equipment in self.in_storage.keys():
            if count < self.in_storage.get(equipment):
                self.in_storage[equipment] -= count
                print(f'Со склада изъято {equipment} в количестве {count} шт., осталось '
                      f'{self.in_storage.get(equipment)} шт.')
            elif count == self.in_storage.get(equipment):
                self.in_storage.pop(equipment)
                print(f'Со склада полностью изъят {equipment} в количестве {count} шт.')
            else:
                print(f'{equipment} отсутствует на складе в достаточном количестве')


general_storage = Storage()
user_printer = Printer('Принтер', True)
user_scanner = Scanner('Сканер', False)
user_copier = Copier('Ксерокс', 50)

general_storage.take_to_storage(user_printer, 50)
general_storage.take_to_storage(user_scanner, 10)
general_storage.take_to_storage(user_copier, 25)

general_storage.take_from_storage(user_printer, Check.number_take('Сколько принтеров вы хотите забрать? >>> '))
general_storage.take_from_storage(user_scanner, Check.number_take('Сколько сканеров вы хотите забрать? >>> '))
general_storage.take_from_storage(user_copier, Check.number_take('Сколько ксероксов вы хотите забрать? >>> '))

print(general_storage)
