# Задача 6. Определение количества дней для бегуна для достижения требуемой дистанции

# в задаче комментированием убраны 2 строки для вывода ежедневной дистанции (13 и 17)

# запрашиваем данные от пользователя по начальной дистанции и целевой
distance = int(input('Введите расстояние на которое пробежал спортсмен в 1-й день >>> '))
target_distance = int(input('Введите расстояние которое хочет пробежать спортсмен >>> '))

day = 1  # выставляем счетчик на 1 для ситуации когда целевая дистанция меньше начальной

# запускаем цикл для достижения требуемой дистанции
while distance < target_distance:
    # print(f'{day}-й день, дистанция {distance:.2f}')  # для последовательного вывода результатов за каждый день
    day += 1  # увеличиваем счетчик дней
    distance *= 1.1  # дневной прирост по дистанции

# print(f'{day}-й день, дистанция {distance:.2f}') # для последовательного вывода результатов за каждый день

# выводим итоговый результат
print(f'на {day}-й день спортсмен достиг результата не менее {target_distance} км')
