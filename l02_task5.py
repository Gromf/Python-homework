# задача 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.

sequence_list = [7, 5, 3, 3, 2]

while True:
    print(sequence_list)
    while True:

        element = (input('введите новое число последовательности, пустой элемент - завершение списка\n>>> '))
        if element == '':
            exit()
        if element.isdigit():
            element = int(element)
            break
        else:
            print('Введите число')

    element_count = sequence_list.count(element)

    if element_count > 0:
        sequence_list.insert(sequence_list.index(element) + element_count, element)
    else:
        for count in range(len(sequence_list)):
            if sequence_list[count] < element:
                sequence_list.insert(count, element)
                break
            if count + 1 == len(sequence_list):
                sequence_list.append(element)
