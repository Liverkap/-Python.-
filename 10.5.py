#               ВЛОЖЕННЫЕ СЛОВАРИ

# Словари могут содержать другие словари, которые сами, в свою очередь, содержат словари, и так далее на любую глубину.
# Такие словари называются вложенными словарями (мы уже сталкивались с вложенными списками и кортежами).
# Вложенные словари – один из способов представления структурированной информации


#           **********          Создание вложенных словарей     *************

# info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
#         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
#         'emp3': {'name': 'Rustam', 'job': 'Tester'}}
#
# print(info)


# Тот же самый словарь info может быть создан по другому:

# info = dict(emp1 = {'name': 'Timur', 'job': 'Teacher'},
#             emp2 = {'name': 'Ruslan', 'job': 'Developer'},
#             emp3 = {'name': 'Rustam', 'job': 'Tester'})
#
# print(info)

# Тот же самый словарь info может быть создан еще так:

# ids = ['emp1', 'emp2', 'emp3']
#
# emp_info = [{'name': 'Timur', 'job': 'Teacher'},
#             {'name': 'Ruslan', 'job': 'Developer'},
#             {'name': 'Rustam', 'job': 'Tester'}]
#
# info = dict(zip(ids, emp_info))
#
# print(info)

# Число уровней вложенности словарей неограниченно!


#       **********************      Обращение к элементам вложенного словаря    ***************

# Для того, чтобы получить значения определенных элементов во вложенном словаре, необходимо указать их ключи в нескольких
# квадратных скобках подобно тому, как мы получали значения во вложенных списках.

# info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
#         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
#         'emp3': {'name': 'Rustam', 'job': 'Tester'}}
#
# print(info['emp1']['name'])
# print(info['emp2']['job'])

# При попытке обращения по несуществующему ключу возникнет ошибка KeyError. Для того, чтобы избежать возникновения такой
# ошибки, используйте словарный метод get(), который по умолчанию возвращает значение None, если ключ отсутствует в словаре.



#         *******************         Изменение вложенных словарей        **********************

# Чтобы изменить значение определенного элемента во вложенном словаре, необходимо обратиться к его ключу и использовать оператор присвоения (=).

# info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
#         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
#         'emp3': {'name': 'Rustam', 'job': 'Tester'}}
#
# info['emp1']['job'] = 'Manager'
#
# print(info['emp1'])



#               ******************     Итерация по вложенным словарям          ********

# info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
#         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
#         'emp3': {'name': 'Rustam', 'job': 'Tester'}}
#
# for emp in info:
#     print('Employee ID:', emp)
#     for key in info[emp]:
#         print(key + ':', info[emp][key])
#     print()


# Аналогичного результата можно было добиться с помощью метода items():
# info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
#         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
#         'emp3': {'name': 'Rustam', 'job': 'Tester'}}
#
# for emp, inf in info.items():
#     print('Employee ID:', emp)
#     for key in inf:
#         print(key + ':', inf[key])
#     print()


#       **************      Генераторы словарей     *************
#
# squares = {i: i**2 for i in range(6)}

            # Общий вид генератора словаря следующий:
            # {ключ: значение for переменная in последовательность}

# где переменная — имя некоторой переменной, последовательность — последовательность значений, которые она принимает (любой итерируемый объект),
# ключ: значение — некоторое выражение, как правило, зависящее от использованной в списочном выражении переменной, которой будут заполнены элементы словаря.


# 1. Генератор словаря при итерировании по строке.

# dct = {c: c * 3 for c in 'ORANGE'}
#
# print(dct)

# 2. Для вычисления ключа и значения в генераторе словаря могут быть использованы выражения.
#
# В следующем примере для вычисления ключа используется метод lower(), а для вычисления значения – метод upper().

# lst = ['ReD', 'GrEeN', 'BlUe']
# dct = {c.lower(): c.upper() for c in lst}
#
# print(dct)

# 3. Извлечение из словаря элементов с определенными ключами.

# dict1 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
# selected_keys = [0, 2, 5]
#
# dict2 = {k: dict1[k] for k in selected_keys}
#
# print(dict2)

#             *******      Условия в генераторе словарей     ******

# squares = {i: i**2 for i in range(10) if i % 2 == 0}
#
# print(squares)

# Не забываем про возможность указания шага в функции range(). Предыдущий код можно записать и без условного оператора: squares = {i: i**2 for i in range(0, 10, 2)}


#            *********       Генераторы вложенных словарей    ****************

# squares = {i: {j: j**2 for j in range(i + 1)} for i in range(5)}
#
# for value in squares.values():
#     print(value)
#
# print(squares)

# *****************************
# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
#
# result = {i: numbers[i] ** 2 for i in range(len(numbers))}

# *************************
# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
#
# result = {key: value for key, value in colors.items() if value is not None}

# **********************************
# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62,
#                     'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654,
#                     'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
#
# result = {key: value for key, value in favorite_numbers.items() if len(str(value)) == 2}

#*****************************
# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
#
# result = {value: key for key, value in months.items()}

# ****************************
# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
#
# result = {int(el.split(':')[0]): el.split(':')[1] for el in s.split()}

#**************************
# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
#
# result = {int(k): v for k, v in [l.split(':') for l in s.split()]}

numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

result = {el: [j for j in range(len(numbers))] for el in numbers if el // 2 == 0}

print(result)









