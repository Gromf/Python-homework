# Задача 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и
# снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.

# функция суммирования и завершения программы
def summation(total_sum, numbers, end_count):
    total_sum += sum(numbers)
    if end_count:
        print(f'Итоговая сумма = {total_sum}')
        exit()
    return total_sum


# функция извлечения чисел из строки и знака остановки "!". Все не числа игнорируются
def take_numbers(user_string):
    user_string = user_string.split()
    user_numbers = []
    for count in range(len(user_string)):
        if user_string[count] == '!':
            end_count = True
            return user_numbers[:count], end_count
        try:
            user_numbers.append(float(user_string[count]))
        except ValueError:
            continue
    end_count = False
    return user_numbers, end_count


total_amount = 0
ending = False
while True:
    take_string = input('Введите числа через пробел, ! для завершения >>> ')
    number, ending = take_numbers(take_string)
    total_amount = summation(total_amount, number, ending)
    print(f'Промежуточная сумма = {total_amount}')


