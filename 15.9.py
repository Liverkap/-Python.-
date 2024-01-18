#                                       функции any(), all(), zip(), enumerate()

#               *************   Функции all() и any()       *******
# При работе с коллекциями часто приходится определять, выполняется ли некоторое условие одновременно для всех элементов
# последовательности или хотя бы для одного. Для этого существуют две встроенные функции all() и any()

#               ***********     Функция all()           *****

# Встроенная функция all() возвращает значение True, если все элементы переданной ей последовательности (итерируемого объекта) истинны (приводятся к значению True), и False в противном случае
#
# Сигнатура функции следующая: all(iterable). В качестве iterable может выступать любой итерируемый объект:
#
# список;
# кортеж;
# строка;
# множество;
# словарь и т.д.

# print(all([True, True, True]))     #  возвращает True, так как все значения списка равны True
# print(all([True, True, False]))    #  возвращает False, так как не все значения списка равны True

# Напомним, что в Python все следующие значения приводятся к значению False:
#
# константы None и False;
# нули всех числовых типов данных: 0, 0.0, 0j, Decimal(0), Fraction(0, 1);
# пустые коллекции: '', (), [], {}, set(), range(0)

# print(all([1, 2, 3]))
# print(all([1, 2, 3, 0, 5]))
# print(all([True, 0, 1]))
# print(all(('', 'red', 'green')))
# print(all({0j, 3+4j}))

# При работе со словарями функция all() проверяет на соответствие параметрам True ключи словаря, а не их значения

# dict1 = {0: 'Zero', 1: 'One', 2: 'Two'}
# dict2 = {'Zero': 0, 'One': 1, 'Two': 2}
#
# print(all(dict1))
# print(all(dict2))

# Обратите внимание: если переданный итерируемый объект пустой, то функция all() возвращает значение True

# print(all([]))          #  передаем пустой список
# print(all(()))          #  передаем пустой кортеж
# print(all(''))          #  передаем пустую строку
# print(all([[], []]))    #  передаем список, содержащий пустые списки
#
#
# #                  ***********      Функция any()       ****
#
# # Встроенная функция any() возвращает значение True, если хотя бы один элемент переданной ей последовательности (итерируемого объекта) является истинным (приводится к значению True), и False в противном случае
# print(any([False, True, False]))       #  возвращает True, так как есть хотя бы один элемент, равный True
# print(any([False, False, False]))

# print(any([0, 0, 0]))
# print(any([0, 1, 0]))
# print(any([False, 0, 1]))
# print(any(['', [], 'green']))
# print(any({0j, 3+4j, 0.0}))

# При работе со словарями функция any() проверяет на соответствие True ключи словаря, а не их значения

# dict1 = {0: 'Zero'}
# dict2 = {'Zero': 0, 'One': 1}
#
# print(any(dict1))
# print(any(dict2))

# Обратите внимание: если переданный объект пуст, то функция any() возвращает значение False

# print(any([]))          #  передаем пустой список
# print(any(()))          #  передаем пустой кортеж
# print(any(''))          #  передаем пустую строку
# print(any([[], []]))    #  передаем список, содержащий пустые списки


#               *****************       Функции all() и any() в связке с функцией map()       *******

# Функции all() и any() могут быть полезны в комбинации с функцией map(), которая может преобразовывать элементы
# последовательности (итерируемого объекта) к значению True/False в соответствии с неким условием

# Приведенный ниже код, проверяет, все ли элементы списка numbers больше 10
# numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]
#
# result = all(map(lambda x: True if x > 10 else False, numbers))
#
# if result:
#     print('Все числа больше 10')
# else:
#     print('Хотя бы одно число меньше или равно 10')
#
# # Лямбда функцию, которая преобразует элементы списка numbers в значения True/False можно упростить следующим образом
# result = all(map(lambda x: x > 10, numbers))

# Приведенный ниже код, проверяет, что хотя бы один элемент списка четное число
# numbers = [17, 91, 78, 55, 231, 45, 5, 89, 99, 11, 19]
#
# result = any(map(lambda x: x % 2 == 0, numbers))
#
# if result:
#     print('Хотя бы одно число четное')
# else:
#     print('Все числа нечетные')

#       *********************       Функция enumerate()     *************
# Встроенная функция enumerate() возвращает кортеж из индекса элемента и самого элемента переданной ей последовательности (итерируемого объекта)
# С помощью необязательного параметра start можно задать начальное значение индекса. По умолчанию значение параметра start = 0, то есть счет начинается с нуля

# colors = ['red', 'green', 'blue']
#
# for pair in enumerate(colors):
#     print(pair)
#
# # Если счет нужно начать с отличного от нуля числа, то нужно передать значение аргумента start
# colors = ['red', 'green', 'blue']
#
# for pair in enumerate(colors, 100):
#     print(pair)

# Обратите внимание, функция enumerate() возвращает не список, а специальный объект, который называется итератором.
# Такой объект похож на список тем, что его можно перебирать циклом for, то есть итерировать. Итератор можно преобразовать в список с помощью функции list()

# colors = ['red', 'green', 'blue']
#
# pairs = enumerate(colors)
#
# print(pairs)
# print(list(pairs))

# Мы также можем использовать распаковку кортежей при итерировании с помощью цикла for
# colors = ['red', 'green', 'blue']
# for index, item in enumerate(colors):
#     print(index, item)
# # Такой код является альтернативой коду
# colors = ['red', 'green', 'blue']
# for i in range(len(colors)):
#     print(i, colors[i])

#           ************        Функция zip()       ****************
# Встроенная функция zip() объединяет отдельные элементы из каждой переданной ей последовательности (итерируемого объекта) в кортежи

# Сигнатура функции следующая: zip(*iterables). В качестве iterable может выступать любой итерируемый объект

# numbers = [1, 2, 3]
# words = ['one', 'two', 'three']
#
# for pair in zip(numbers, words):
#     print(pair)

# Функция zip(), как и функция enumerate() возвращает не список, а специальный объект, который называется итератором.
# Такой объект похож на список тем, что его можно перебирать циклом for, то есть итерировать. Итератор можно преобразовать в список с помощью функции list()

# Мы можем передавать функции zip() сколько угодно итерируемых объектов
# numbers = [1, 2, 3]
# words = ['one', 'two', 'three']
# romans = ['I', 'II', 'III']
#
# result = zip(numbers, words, romans)
# print(list(result))

# Мы можем передать функции zip() даже один итерируемый объект
# numbers = [1, 2, 3]
# result = zip(numbers)
# print(list(result))

# Если функции zip() передать итерируемые объекты, имеющие разную длину, то объект с наименьшим количеством элементов определяет итоговую длину

# numbers = [1, 2, 3, 4]
# words = ['one', 'two']
# romans = ['I', 'II', 'III']
#
# result = zip(numbers, words, romans)
# print(list(result))

#                   *********       Частые сценарии использования функции zip()     ****

# Сценарий 1. Функция zip() удобна для создания словарей, когда ключи и значения находятся в разных списках
# keys = ['name', 'age', 'gender']
# values = ['Timur', 28, 'male']
#
# info = dict(zip(keys, values))
# print(info)

# Сценарий 2. Функция zip() удобна для одновременного (параллельного) итерирования сразу по нескольким коллекциям.

# name = ['Timur', 'Ruslan', 'Rustam']
# age = [28, 21, 19]
#
# for x, y in zip(name, age):
#     print(x, y)

# Примечание 1. Итераторы – важная концепция языка Python. Нужно помнить:
#
# итераторы можно обойти циклом for;
# итератор можно преобразовать в список или кортеж, с помощью функций list() и tuple();
# итератор можно распаковать с помощью *.

# Примечание 2. Реализация встроенных функций all() и any() выглядит примерно так:
# def all(iterable):
#     for item in iterable:
#        if not item:
#            return False
#     return True
#
# def any(iterable):
#     for item in iterable:
#         if item:
#             return True
#     return False

# Примечание 3. Мы можем использовать одновременно функции zip() и enumerate()
# list1 = ['a1', 'a2', 'a3']
# list2 = ['b1', 'b2', 'b3']
#
# for index, (item1, item2) in enumerate(zip(list1, list2)):
    # print(index, item1, item2)

# ********
# numbers = [1, 2, 3, 4, 5, 6]
#
# for index, elem in enumerate(numbers):
#     if elem % 2 == 0:
#         numbers[index] *= 2
#
# print(numbers)

# **********
# numbers = [10, 30, 20, 50, 40, 60, 70, 80]
#
# total = 0
# for index, number in enumerate(numbers, 1):
#     if index % 2 == 0:
#         total += number
# print(total)

# ********
# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 4, 3, 2, 1]
#
# result = 0
# for x, y in zip(list1, list2):
#     result += x*y
# print(result)

# ******
# words1 = ['яблоко', 'ананас', 'апельсин', 'хурма', 'гранат', 'мандарин', 'айва']
# words2 = ['林檎', 'パイナップル', 'オレンジ', '柿']
# words3 = ['apple', 'pineapple', 'orange', 'persimmon', 'pomegranate']
#
# print(len(list(zip(words1, words2, words3))))

# **********
# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#     return any(map(lambda x: x in command, ignore))
#
#
# print(ignore_command('get ip'))
# print(ignore_command('select all'))
# print(ignore_command('delete'))
# print(ignore_command('trancate'))

# *******
# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
#
#
# for country, city, popul in zip(countries, capitals, population):
#     print(f'{city} is the capital of {country}, population equal {popul} people.')
#
# # ********(ОТ ПОЛЬЗОВАТЕЛЯ)
# for data in zip(countries, capitals, population):
#     print('{1} is the capital of {0}, population equal {2} people.'.format(*data))


# ВНУТРИ ШАРА

# abscissas = [float(num) for num in input().split()]
# ordinates = [float(num) for num in input().split()]
# applicates = [float(num) for num in input().split()]
#
# R = 2
#
# res = all(list(map(lambda x: x[0] ** 2 + x[1] ** 2 + x[2] ** 2 <= R ** 2, zip(abscissas, ordinates, applicates))))
# print(res)
#
# # ВНУТРИ ШАРА(ОТ ПОЛЬЗОВАТЕЛЯ)
# abscissas = list(map(float, input().split()))
# ordinates = list(map(float, input().split()))
# applicates = list(map(float, input().split()))
#
# print(all(map(lambda x, y, z: x**2 + y**2 + z**2 <= 4, abscissas, ordinates, applicates)))


# КОРРЕКТНЫЙ IP АДРЕС

# print(all(map(lambda x: x.isdigit() and int(x) <= 255, [num for num in input().split('.')])))

# КОРРЕКТНЫЙ IP АДРЕС(ОТ ПОЛЬЗОВАТЕЛЯ)
# print(all(x.isdigit() and int(x) < 256 for x in input().split('.')))


# ИНТЕРЕСНЫЕ ЧИСЛА

# a, b = int(input()), int(input())
# a = int(input())

# a_list = [int(num) for num in input() if num != '0']
# b_list = [int(num) for num in input() if num != '0']
# print(a_list)
# print(b_list)

# div_num = set(int(num) for num in str(a) if num != '0') | set(int(num) for num in str(b) if num != '0')
# print(div_num)

# def check(num):
#     return lambda x: num % int(x) == 0, str(num)
#
# numbers = list(range(a, b + 1))
# li = list(filter(check, numbers))
# print(li)
#
# # res = list(map(, div_num, numbers))
# # k = []
# # for num in numbers:
# #     if all(num % int(x) == 0 for x in str(num)):
# #         k.append(num)
# #
# # print(k)

# numbers = [i for i in range(int(input()), int(input()) + 1) if '0' not in list(str(i))]
#
# def check(num):
#     return all(map(lambda el: num % int(el) == 0, str(num)))
#
# print(*filter(check, numbers))

# ИНТЕРЕСНЫЕ ЧИСЛА(ОТ ПРЕПОДАВАТЕЛЯ)
# a, b = int(input()), int(input())
#
# for i in range(a, b + 1):
#     # создаем кортеж со всеми цифрами числа
#     digits = tuple(map(int, str(i)))
#     print(digits)
#
#     # проверяем, что число не содержит 0 и делится на все свои цифры
#     if 0 not in digits and all(map(lambda cur_digit: i % cur_digit == 0, digits)):
#         print(i, end=" ")


# ИНТЕРЕСНЫЕ ЧИСЛА(ОТ ПОЛЬЗОВАТЕЛЯ)
# def check(num):
#     return all(map(lambda x: int(x) and num % int(x) == 0, str(num)))
#
# a, b = int(input()), int(input())
# seq = range(a, b + 1)
# print(*list(filter(lambda x: check(x), seq)))


# ХОРОШИЙ ПАРОЛЬ

# password = input()
#
# psw = all([len(password) >= 7, any(map(lambda x: x.isdigit(), password)), any(map(lambda x: x.islower(), password)), any(map(lambda x: x.isupper(), password))])
#
# if psw:
#     print('YES')
#
# else:
#     print('NO')

# ХОРОШИЙ ПАРОЛЬ(ОТ ПОЛЬЗОВАТЕЛЯ)
# s = input()
# print('YES' if all((any(i.isupper() for i in s),
#                     any(i.islower() for i in s),
#                     any(i.isdigit() for i in s),
#                     len(s) >= 7)) else 'NO')
#
# # ХОРОШИЙ ПАРОЛЬ(ОТ ПОЛЬЗОВАТЕЛЯ)
# s = input()
# print(('YES', 'NO')[any([len(s) < 7, s.islower(), s.isupper(),s.isalpha(), s.isdigit()])])


# ХОРОШИЙ ПАРОЛЬ(ОТ ПОЛЬЗОВАТЕЛЯ)
# def is_good_password(password):
#     if len(password) < 7:         # Проверяем пароль на длину
#         return "NO"
#     flag = [False, False, False]  # Создаём флаг-список для проверки пароля на наличие определённых элементов
#     for i in password:
#         if all(flag):             # Если все значения станут равны True до прохода по всему паролю, прерываем функцию
#             return "YES"
#         elif i.isdigit():         # Если элемент является цифрой, меняем нулевой элемент флаг-списка на True
#             flag[0] = True
#         elif i.isupper():         # Если элемент является заглавной буквой, меняем первый элемент флаг-списка на True
#             flag[1] = True
#         elif i.islower():         # Если элемент является строчной буквой, меняем второй элемент флаг-списка на True
#             flag[2] = True
#     if all(flag):                 # После завершения цикла проверяем флаг-список, чтобы все значения были равны True
#         return "YES"
#     return "NO"
#
#
# qwerty = input()
# print(is_good_password(qwerty))


# ОТЛИЧНИКИ

classes = int(input())

new_list = []

for classes in range(classes):
    cur_list = []
    for j in range(int(input())):
        cur_list.append(input().split())
    new_list.append(cur_list)

print(new_list)





# classes, students = int(input()), int(input())
# # my_list = [i for i in input().split()]
# # print(my_list)
#
# new_list = []
#
# for classes in range(classes):
#     for j in range(students):
#         new_list.append(input().split())
#
# print(new_list)



# for i in range(students):
#     std = dict()
#     x = input().split()
#     std[x[1]] = x[0]
#     my_list.append(std)


