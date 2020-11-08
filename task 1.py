# Задача 1. Работа с переменными

# создаем переменные разных типов с заданными значениями
variable_int = 15
variable_text = 'random text'
variable_bool = True
variable_float = 5.57
variable_list = [5, 10, 4.57, 'hello world']

# выводим на экран значения переменных выше
print('Значение переменной целое число = ', variable_int)
print('Значение переменной текст = ', variable_text)
print('Значение переменной логическое значение = ', variable_bool)
print('Значение переменной дробное число = ', variable_float)
print('Значение переменной список 0 элемент = ', variable_list[0])
print('Значение переменной список 3 элемент = ', variable_list[3])

# предлагаем пользователю ввести значения в переменные, 2 из них переводим в числовые значения
user_variable_int = int(input('Введите целое число >>> '))
user_variable_text = input('Введите текст >>> ')
user_variable_float = float(input('Введите дробное или целое число >>> '))

# выводим значения введенных ранее переменных
print('Вы ввели целое чило = ', user_variable_int)
print('Вы ввели текст = ', user_variable_text)
print('Вы ввели число = ', user_variable_float)
