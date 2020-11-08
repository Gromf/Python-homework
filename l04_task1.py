"""
Задача 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.
"""

# Для запуска необходимо передать 3 параметра в целых числах:

from sys import argv


def salary(worked_time, remuneration_per_hour, award):
    return worked_time * remuneration_per_hour + award


try:
    script_name, work_time, salary_per_hour, bonus = argv
    work_time = int(work_time)
    salary_per_hour = int(salary_per_hour)
    bonus = int(bonus)
except ValueError:
    print('Передайте в параметрах 3 числа')
    exit()

if work_time < 0 or salary_per_hour < 0:
    print('Зарплата или рабочее время не могут быть отрицательными')
    exit()

print(salary(work_time, salary_per_hour, bonus))
