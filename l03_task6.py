# Задача 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

# т.к. по условию не понятно какие должны быть входные данные, то я считаю, что любые кроме написанных
# маленькими латинскими буквами должны игнорироваться и требовать повторный ввод

# кроме этого не понятно, как должен выполняться перевод 1-й буквы большую - через встроенную функцию или нет,
# реализовал оба варианта


# функция проверки на корректность ввода
def english_check(checking_user_string):
    letters = set(checking_user_string)  # превращаем строку в множество
    english_letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', ' ')
    set_count = 0
    for letter in letters:  # проверяем, что все элементы множества входят в словарь
        if letter in english_letters:
            set_count += 1
    if set_count == len(letters):
        return True
    else:
        return False


def upper_included(user_word):
    return user_word.title()


# функция перевода 1-й буквы слова в верхний регистр без использования встроенной
def upper(user_word):
    english_letters = {
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K',
        'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V',
        'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'
    }
    upper_word = english_letters.get(user_word[0]) + user_word[1:]
    return upper_word


while True:
    user_string = input('Введите слова маленькими латинскими буквами\n>>> ')
    if english_check(user_string):
        break
    print('Введите еще раз')

words = user_string.split()
title_words = []


for count in range(0, len(words)):
    title_words.append(upper(words[count]))
    words[count] = upper_included(words[count])

print('Через встроенную функцию')
print(' '.join(words))
print('Без встроенной функции')
print(' '.join(title_words))

