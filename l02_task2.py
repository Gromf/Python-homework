# Задача 2. Для списка реализовать обмен значений соседних элементов

user_list = []

while True:
    element = input('Введите элемент списка, пустой элемент - завершение списка >>> ')
    if element == '':
        break
    user_list.append(element)

print(user_list)

for count in range(1, len(user_list), 2):
    user_list[count - 1], user_list[count] = user_list[count], user_list[count - 1]

print(user_list)
