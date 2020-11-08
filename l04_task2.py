"""
Задача 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
элемента.
"""

default_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [default_list[count] for count in range(1, len(default_list)) if default_list[count-1] < default_list[count]]

print(default_list)
print(new_list)
