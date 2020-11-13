"""
Задача 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

# судя по условию необходимо в начале записать числа в файл, а потом его открыть и посчитать сумму

with open('task5_new.txt', 'w') as writing_file:
    print(input('Введите числа разделенные пробелами >>> '), file=writing_file)

with open('task5_new.txt') as opened_file:
    line = opened_file.readline()
    line = line.split()
    sum_total = 0
    for number in line:
        try:  # проверка на числа, если пользователь ввел не число, то это значение игнорируется
            sum_total += float(number)
        except ValueError:
            continue

    print(sum_total)
