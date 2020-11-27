"""
Задача 1.Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class WrongForm(Exception):
    def __init__(self, text):
        self.text = text


class Data:

    @staticmethod
    def number_check(date: list):
        months = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31,
                  4: 30, 6: 30, 9: 30, 11: 30, 2: 28}
        try:
            date[0] = int(date[0])
            date[1] = int(date[1])
            date[2] = int(date[2])
        except ValueError:
            print('В дате необходимо передавать числа')
            exit(1)
        try:
            error = ''
            if date[1] > 12 or date[1] < 1:
                error += f'Месяц указан некорректно, необходимо указать от 1 до 12, а не {date[1]}\n'
            elif date[0] > months.get(date[1]):
                error += f'В месяце {date[1]} не больше {months.get(date[1])} дней, a не {date[0]}\n'
            if date[2] < 1:
                error += 'Год должен быть больше 0'
            if error != '':
                raise WrongForm(error)
            print('Дата корректна')
            return True
        except WrongForm as err:
            print(err)

    @classmethod
    def take_data(cls, data):
        try:
            number = data.split('-')
            if len(number) != 3:
                raise WrongForm('Форма некорректна, необходимо вводить день-месяц-год')
            if cls.number_check(number):
                return data
            else:
                return ''
        except WrongForm as err:
            print(err)

    def __init__(self, data):

        self.data = Data.take_data(data)

    def __str__(self):
        if self.data is not None:
            return self.data
        else:
            return 'Корректная дата не введена'


# test_data = Data('01-05-2020')

user_data = Data(input('Введите дату в формате день-месяц-год, например, 01-05-2020 >>> '))
print(user_data)
