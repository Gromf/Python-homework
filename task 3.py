# Задача 3. Ввод числа n и вывод суммы чисел n + nn + nnn

# запрашиваем число n от пользователя
user_number = input('Введите значение n для отображения суммы n + nn + nnn >>> ')

# пользуемся тем, что user_number это строка, собираем n, nn и nnn как их сумму, а потом переводим их в число

n = int(user_number)
nn = int(user_number + user_number)
nnn = int(user_number + user_number + user_number)

user_sum = n + nn + nnn

print(f'Сумма {n} + {nn} + {nnn} = {user_sum}')
