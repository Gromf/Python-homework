"""
Задача 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

# заранее создан файл task3_def.txt

with open('task3_def.txt') as opened_file:
    average_salary = 0
    for worker in opened_file:
        worker_data = worker.split(':')
        worker_salary = float(worker_data[1].replace('\n', '').replace(' ', ''))
        if worker_salary >= 20000:
            print(f'У сотрудника {worker_data[0]} зарплата больше 20000')
        average_salary += worker_salary
    average_salary /= len(worker)
    print(f'Средняя зарплата всех сотрудников = {average_salary:.2f}')
