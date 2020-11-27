# Задача 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

# Задача реализован через словари. Есть 2 аналогичные функции: одна запрашивает все параметры, вторая словарь

# функция по сбору итоговой информации о пользователе, принимает
def user_data(first_name, last_name, year_birth, city_residence, email, phone):
    user_temp_data = (first_name, last_name, year_birth, city_residence, email, phone)
    count = 0
    user_temp_info = ''
    for values in user_parameter.values():
        user_temp_info += values + ': ' + user_temp_data[count] + '; '
        count += 1
    return user_temp_info


# сборка словаря с информацией о пользователе
def take_user_data(user_current_parameter):
    while True:
        user_info = input(f'Введите параметр пользователя: {user_current_parameter} >>> ')
        if user_info == '':
            print('Ошибка ввода, повторите')
        else:
            return user_info


# справочный словарь с параметрами пользователя
user_parameter = {
    'name': 'Имя',
    'last_name': 'Фамилия',
    'year_birth': 'Год рождения',
    'city_residence': 'Город проживания',
    'email': 'email',
    'phone': 'Телефон'
}
user = {}

for key, value in user_parameter.items():
    user[key] = take_user_data(value)

# вывод информации на экран
print('Вывод через функцию user_data')
print(user_data(
    first_name=user.get('name'), last_name=user.get('last_name'), year_birth=user.get('year_birth'),
    city_residence=user.get('city_residence'), email=user.get('email'), phone=user.get('phone'))
)


# аналог первой функции, но принимает словарь, масштабируется под любое кол-во параметров
def user_data_light(**user_info):
    user_temp_info = ''
    for keys, values in user_parameter.items():
        user_temp_info += values + ': ' + user_info.get(keys) + '; '
    return user_temp_info


# вывод лайт версии
print('Вывод через функцию user_data_light')
print(user_data_light(**user))
