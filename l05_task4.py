"""
Задача 4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

"""

# заранее создан файл task4_def.txt

ru_eng_translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('task4_def.txt') as opened_file:
    with open('task4_new.txt', 'w') as writing_file:
        for line in opened_file:
            for key, value in ru_eng_translate.items():
                if line.count(key) > 0:
                    writing_file.write(line.replace(key, value))
                    break
