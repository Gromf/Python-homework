# Задача 6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно
# сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

# создаем список товаров
goods_list = []
count = 1
# кортеж со структурой для словаря товара
structure = (('название', 'text'),
             ('цена', 'number',),
             ('количество', 'number'),
             ('ед', 'text'))

while True:
    # вводим название товара и проверяем на пустое для завершения списка
    goods_property = input('Введите название товара, пусто для завершения списка >>> ')
    if goods_property == '':
        break
    goods = {'название': goods_property}

    # формируем словарь с товаром
    for element in range(1, len(structure)):

        # определяем тип значений - число или текст и ожидаем ввод
        if structure[element][1] == 'number':
            while True:
                goods_property = input(f'Введите {structure[element][0]} товара числом >>> ')
                if goods_property.isdigit():
                    goods[structure[element][0]] = int(goods_property)
                    break
                else:
                    print('Введите число')
        else:
            while True:
                goods_property = input(f'Введите {structure[element][0]} товара >>> ')
                if goods_property != '':
                    break
            goods[structure[element][0]] = goods_property

    # формируем кортеж из номера и словаря
    goods_list.append((count, goods))
    count += 1

# выводим список кортежей
print('Список товаров:')
print(*goods_list, sep='\n')

# формируем словарь для анализа
analytical_dict = {}

for key_count in range(0, len(structure)):
    analytical_temp = []
    for goods_count in goods_list:
        analytical_temp.append(goods_count[1].get(structure[key_count][0]))
    analytical_temp = list(set(analytical_temp))  # удаляем дубликаты
    analytical_dict[structure[key_count][0]] = analytical_temp

# выводим итоговый словарь
print('Аналитический словарь:')
for key, value in analytical_dict.items():
    print(f"{key} - {value}")
