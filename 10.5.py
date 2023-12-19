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

# ******************
# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
#
# result = {el: [j for j in range(1, el + 1) if el % j == 0] for el in numbers}

# **********(ОТ ПОЛЬЗОВАТЕЛЯ)
# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
#
# result = {n: [i for i in range(1, n // 2 + 1) if n % i == 0] + [n] for n in numbers}

# ***********
# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
#
# result = {el: [ord(ch) for ch in el] for el in words}

# ******** (ОТ ПОЛЬЗОВАТЕЛЯ)(ЧЕРЕЗ map)

# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
#
# result = {el: list(map(ord, el)) for el in words}

# ***********
# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
#            13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
#
# result = {key: value for key, value in letters.items() if key not in remove_keys}

# *********** (ОТ ПОЛЬЗОВАТЕЛЯ)(ЧЕРЕЗ МНОЖЕСТВА)
# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
#            13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
#
# result = {k: letters[k] for k in set(letters) - set(remove_keys)}

# # ***************
# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50),
#             'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78),
#             'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80),
#             'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
#
# result = {key: value for key, value in students.items() if value[0] > 167 and value[1] < 75}

# ************
# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24),
#           (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
# result = {el[0]: el[1:] for el in tuples}

# *********(ОТ ПОЛЬЗОВАТЕЛЯ)(РАСПАКОВКА КОРТЕЖА В ПЕРЕМЕННУЮ)
# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24),
#           (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
# result = {i: (*j,) for i, *j in tuples}

# ***********
# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
#
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti',
#                  'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
#
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

# result = [{s_id: {name: grade}} for s_id, name, grade in zip(student_ids, student_names, student_grades)]






















