"""
Задача 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
по нему. Вывести словарь на экран.
"""

# заранее создан файл task6_def.txt

with open('task6_def.txt') as opened_file:
    lesson_dic = {}
    for line in opened_file:
        lesson = line.split(':')
        lesson_count = 0
        for number in lesson[1].split():
            try:
                lesson_count += int((number[:number.index('(')]).replace(' ', ''))
            except ValueError:
                continue
        lesson_dic[lesson[0]] = lesson_count

print(lesson_dic)
