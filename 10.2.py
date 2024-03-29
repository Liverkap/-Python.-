#                                        Основы работы со словарями

#           ********************        Функция len()   ****************
# fruits = {'Apple': 70, 'Grape': 100, 'Banana': 80}
# capitals = {'Россия': 'Москва', 'Франция': 'Париж'}
#
# print(len(fruits))
# print(len(capitals))

#               *********** Оператор принадлежности in  **

# Оператор in позволяет проверить, содержит ли словарь заданный ключ.

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# if 'Франция' in capitals:
#     print('Столица Франции - это', capitals['Франция'])


# Оператор принадлежности in на словарях работает очень быстро, намного быстрее, чем на списках, поэтому если нужен многократный поиск в коллекции данных, словарь – подходящий выбор.


#                       **************************  Встроенные функции sum(), min(), max()  *************


# Встроенная функция sum() принимает в качестве аргумента словарь с числовыми ключами и вычисляет сумму его ключей
# Для корректной работы функции sum() ключами словаря должны быть именно числа.
#
# my_dict = {10: 'Россия', 20: 'США', 30: 'Франция'}
#
# print('Сумма всех ключей словаря =', sum(my_dict))


# Встроенные функции min() и max() принимают в качестве аргумента словарь и находят минимальный и максимальный ключ соответственно,
# при этом ключ может принадлежать к любому типу данных, для которого возможны операции порядка <, <=, >, >= (числа, строки, и т.д.).

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# months = {1: 'Январь', 2: 'Февраль', 3: 'Март'}
#
# print('Минимальный ключ =', min(capitals))
# print('Максимальный ключ =', max(months))


#                   ************************    Сравнение словарей    ********
# ловари можно сравнивать между собой. Равные словари имеют одинаковое количество элементов и содержат равные элементы (ключ: значение). Для сравнения словарей используются операторы == и !=.

# months1 = {1: 'Январь', 2: 'Февраль'}
# months2 = {1: 'Январь', 2: 'Февраль', 3: 'Март'}
# months3 = {3: 'Март', 1: 'Январь', 2: 'Февраль'}
#
# print(months1 == months2)
# print(months2 == months3)
# print(months1 != months3)



# Примечание 1. Обращение по индексу и срезы недоступны для словарей
# Примечание 2. Операция конкатенации + и умножения на число * недоступны для словарей.
# Примечание 3. Словари нужно использовать в следующих случаях:
#       -Подсчет числа каких-то объектов. В этом случае нужно завести словарь, в котором ключи — названия объектов, а значения — их количество.
#       -Хранение каких-либо данных, связанных с объектом. Ключи — наименования объектов, значения — связанные с ними данные. Например, если нужно по названию месяца определить его порядковый номер, то это можно сделать при помощи словаря num = {'January': 1, 'February': 2, 'March': 3, ...}.
#       -Установка соответствия между объектами (например, “родитель—потомок”). Ключ — объект, значение — соответствующий ему объект.
#       -Если нужен обычный список, где максимальное значение индекса элемента очень велико, но при этом используются не все возможные индексы (так называемый “разреженный список”), то для экономии памяти можно использовать словарь.


# my_dict = {'foo': 100, 'bar': 200, 'baz': 300}
#
# print(my_dict['bar':'baz'])

# my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}
#
# print(min(my_dict) + max(my_dict))


#                                                      Перебор элементов словаря

# Перебор элементов словаря осуществляется так же как перебор элементов списка, с помощью цикла for

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for key in capitals:
#     print(key)

# Для вывода значений словаря каждого на отдельной строке можно использовать следующий код:

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for key in capitals:
#     print(capitals[key])

# Для вывода элементов словаря каждого на отдельной строке можно использовать следующий код:

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for key in capitals:
#     print('Столица', key, '- это', capitals[key])


#               **************  Методы keys(), values(), items()    *************

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for key in capitals.keys():     # итерируем по списку ['Россия', 'Франция', 'Чехия']
#     print(key)


# Словарный метод values() возвращает список значений всех элементов словаря.

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for value in capitals.values():     # итерируем по списку ['Москва', 'Париж', 'Прага']
#     print(value)

# Словарный метод items() возвращает список всех элементов словаря, состоящий из кортежей пар (ключ, значение).
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for item in capitals.items():
#     print(item)

# Используя магию распаковки кортежей, можно писать такой код:
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for key, value in capitals.items():
#     print(key, '-', value)


#               ************************    Распаковка ключей словаря   ***********

# Если требуется вывести только значение ключей словаря, то мы также можем использовать операцию распаковки словаря
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# print(*capitals, sep='\n')


#                   **************      Сортировка словаря      *********

# Так как словарь состоит из пар, то и отсортировать его можно как по ключам, так и по значениям.
# Сортировка по ключам выполняется с использованием функции sorted().

# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
#
# for key in sorted(capitals):
#     print(key)


# Для сортировки словаря по значениям можно использовать функцию sorted() вместе с методом items()

# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
#
# for key, value in sorted(capitals.items(), key = lambda x: x[1]):
#     print(value)


# Примечание 1. Как мы уже знаем, с помощью оператора принадлежности in можно быстро проверить наличие ключа в словаре.
# Для проверки наличия значения в словаре можно использовать оператор in вместе с методом values(), который возвращает список всех значений словаря.
# Проверка наличия ключа в словаре:

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# if 'Россия' in capitals:
#     print('В словаре есть ключ Россия')


# Проверка наличия значения в словаре:

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# if 'Париж' in capitals.values():
#     print('В словаре есть значение Париж')

# Примечание 4. Словарные методы items(), keys(), values() возвращают не совсем обычные списки.
# Типы этих списков -  dict_items, dict_keys, dict_values соответственно, в отличие от обычных списков - list.
# Методы обычных списков недоступны для списков типа dict_items, dict_keys, dict_values. Используйте явное преобразование с помощью функции list() для получения доступа к методам списков.


# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

# users_list = []
#
# for i in range(len(users)):
#     if users[i]['phone'][-1:] == '8':
#         users_list.append(users[i]['name'])
#
# print(*sorted(users_list))


# (ОТ ПРЕПОДАВАТЕЛЯ)

# result = [user['name'] for user in users if user['phone'].endswith('8')]
#
# print(*sorted(result))


# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
# result = [user['name'] for user in users if len(user) < 3 or len(user['email']) == 0]
# print(*sorted(result))
#
# # (ОТ ПОЛЬЗОВАТЕЛЯ)
# lst = []
# for n in users:
#     if 'email' not in n or n['email'] == '':
#         lst.append(n['name'])
# print(*sorted(lst))


# СТРОКОВОЕ ПРЕДСТАВЛЕНИЕ

# numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
#
# for el in input():
#     print(numbers[int(el)], end=' ')

# ИНФОРМАЦИЯ ОБ УЧЕБНЫХ КУРСАХ

# courses = {'CS101': ['3004', 'Хайнс', '8:00'],
#            'CS102': ['4501', 'Альварадо', '9:00'],
#            'CS103': ['6755', 'Рич', '10:00'],
#            'NT110': ['1244', 'Берк', '11:00'],
#            'CM241': ['1411', 'Ли', '13:00']}
#
# number = input()
#
# print(f'{number}:', end=' ')
# print(*courses[number], sep=', ')


# ИНФОРМАЦИЯ ОБ УЧЕБНЫХ КУРСАХ (ОТ ПОЛЬЗОВАТЕЛЯ)

# course = {'CS101': ['3004', 'Хайнс', '8:00'],
#           'CS102': ['4501', 'Альварадо', '9:00'],
#           'CS103': ['6755', 'Рич', '10:00'],
#           'NT110': ['1244', 'Берк', '11:00'],
#           'CM241': ['1411', 'Ли', '13:00']}
# n = input()
# aud, teacher, time = course[n]
# print(f'{n}: {aud}, {teacher}, {time}')


# ИНФОРМАЦИЯ ОБ УЧЕБНЫХ КУРСАХ (ОТ ПОЛЬЗОВАТЕЛЯ)
# column_names = ('Номер курса', 'Номер аудитории', 'Преподаватель', 'Время')
# table_values = (
#     ('CS101', '3004', 'Хайнс', '8:00'),
#     ('CS102', '4501', 'Альварадо', '9:00'),
#     ('CS103', '6755', 'Рич', '10:00'),
#     ('NT110', '1244', 'Берк', '11:00'),
#     ('CM241', '1411', 'Ли', '13:00'),
# )
# table_with_column_names = [dict(zip(column_names, row)) for row in table_values]
#
# course_number = input()
#
# for row in table_with_column_names:
#     if row.get('Номер курса') == course_number:
#         print(f"{row.pop('Номер курса')}:", ', '.join(row.values()))
#         break


# НАБОР СООБЩЕНИЙ

# symbols = {1: '.,?!:', 2: 'ABC', 3: 'DEF', 4: 'GHI',5: 'JKL',
#            6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ', 0: ' '}

# symbols = {'.': 1, ',': 11, '?': 111, '!': 1111, ':': 11111,
#            'A': 2, 'B': 22, 'C': 222, 'D': 3, 'E': 33, 'F': 333,
#            'G': 4, 'H': 44, 'I': 444, 'J': 5, 'K': 55, 'L':555,
#            'M': 6, 'N': 66, 'O': 666, 'P': 7, 'Q': 77, 'R': 777, 'S': 7777,
#            'T': 8, 'U': 88, 'V': 888, 'W': 9, 'X': 99, 'Y': 999, 'Z': 9999, ' ': 0}
#
# s = input()
#
# for el in s:
#     if el.upper() in symbols:
#         print(symbols[el.upper()], end='')


# НАБОР СООБЩЕНИЙ (ОТ ПОЛЬЗОВАТЕЛЯ)
# keyboard = {
#     "1": ".,?!:",
#     "2": "ABC",
#     "3": "DEF",
#     "4": "GHI",
#     "5": "JKL",
#     "6": "MNO",
#     "7": "PQRS",
#     "8": "TUV",
#     "9": "WXYZ",
#     "0": " "
# }
#
# for letter in input().upper():
#     for key, value in keyboard.items():
#         if letter in value:
#             print(key * (value.index(letter) + 1), end="")


# КОД МОРЗЕ
# alphabet = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
#             'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
#             'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
#             'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
#             '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
#             '7': '--...', '8': '---..', '9': '----.'}
#
# s = input()
#
# for el in s:
#     if el.upper() in alphabet:
#         print(alphabet[el.upper()], end=' ')

# КОД МОРЗЕ (АВТОСОЗДАНИЕ СЛОВАРЯ)
# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
#          '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
#          '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# alphabet = []
#
# for i in range(len(letters)):
#     alphabet.append([letters[i], morse[i]])
#
# alphabet = dict(alphabet)
#
# s = input()
#
# for el in s:
#     if el.upper() in alphabet:
#         print(alphabet[el.upper()], end=' ')

# КОД МОРЗЕ (БЕЗ СОЗДАНИЯ СЛОВАРЯ)
# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
#          '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
#          '...--', '....-', '.....', '-....', '--...', '---..', '----.']
#
# s = input()
# for el in s:
#     print(morse[letters.index(el.upper())], end=' ')


# КОД МОРЗЕ (ПРЕПОДАВАТЕЛЯ)
# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
#          '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
#          '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# mydict = dict(zip(letters, morse))
# word = input().upper()
#
# for c in word:
#     if c in mydict:
#         print(mydict[c], end=' ')
















