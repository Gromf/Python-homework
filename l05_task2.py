"""
Задача 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

# заранее создан файл task2_def.txt

with open('task2_def.txt') as opened_file:
    line = opened_file.readlines()
    print(f'Количество строк в файле = {len(line)}')
    for line_count in line:
        words = line_count.split()
        print('В строке: ', line_count.replace("\n", ""), f'\nСодержится {len(words)} слов')

# замена \n на пустое и добавление \n сделано для красоты отображения последней строки
