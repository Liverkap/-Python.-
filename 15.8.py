
# numbers = [1, 2, 5, 3, 4]
# numbers.sort(key=lambda x: -x)
# print(numbers)


# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# result = list(filter(lambda: True, primes))
# print(result)

# **************
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# result = list(filter(lambda x: True, primes))
# print(result)
#
# # *************
# full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
# print(full_name('ben', 'affleck'))


# ***********

# func = lambda x: True if x % 19 == 0 or x % 13 == 0 else False
#
# print(func(19))
# print(func(13))
# print(func(20))
# print(func(15))
# print(func(247))

# **************(ОТ ПОЛЬЗОВАТЕЛЯ)(БЕЗ TRUE В УСЛОВИИ)
# func = lambda x: x % 19 == 0 or x % 13 == 0
#
# # ***********(ОТ ПОЛЬЗОВАТЕЛЯ)
# func = lambda n: not (n % 19 * n % 13)

# **************

# func = lambda s: True if s[0].lower() == 'a' and s[-1].lower() == 'a' else False
#
# print(func('abcd'))
# print(func('bcda'))
# print(func('abcda'))
# print(func('Abcd'))
# print(func('bcdA'))
# print(func('abcdA'))

# *********
# is_non_negative_num = lambda s: s.replace('.', '', 1).isdigit()
#
# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))
# print(is_non_negative_num('-18'))
# print(is_non_negative_num('-34.67'))
# print(is_non_negative_num('987'))
# print(is_non_negative_num('abcd'))
# print(is_non_negative_num('123.122.12'))
# print(is_non_negative_num('123.122'))

# ***************(ОТ ПОЛЬЗОВАТЕЛЯ)
# is_non_negative_num = lambda s: s.count('.') <= 1 and set(s) <= set('.1234567890')

# *************
# is_num = lambda s: s.replace('.', '', 1).replace('-', '', 1).isdigit() and s.rfind('-') <= 0
#
# print(is_num('10.34ab'))
# print(is_num('10.45'))
# print(is_num('-18'))
# print(is_num('-34.67'))
# print(is_num('987'))
# print(is_num('abcd'))
# print(is_num('123.122.12'))
# print(is_num('-123.122'))
# print(is_num('--13.2'))
#
# # *************(ОТ ПРЕПОДАВАТЕЛЯ)
# is_non_negative_num = lambda q: q.replace('.', '', 1).isdigit()
#
# is_num = lambda q: is_non_negative_num(q[1:]) if q[0] == '-' else is_non_negative_num(q)
#
# # *********** (ОТ ПОЛЬЗОВАЕТЕЛЯ) в новых версиях Python можно удалять единственный префикс методом строк removeprefix
# is_num = lambda x: x.removeprefix('-').replace('.', '', 1).isdigit()
#
# # ***************(ОТ ПОЛЬЗОВАТЕЛЯ)
# is_num = lambda x: x.replace('-', '', x[0] == '-').replace('.', '', 1).isdigit()


# *************
# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray',
#          'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware',
#          'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond',
#          'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
#
# # new_words = list(filter(lambda x: len(x) == 6, words))
# # print(*sorted(new_words))
#
# # **********(ОТ ПОЛЬЗОВАТЕЛЯ)
# print(*sorted(filter(lambda x: len(x) == 6, words)))


# **************
# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80,
#            93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57,
#            53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94,
#            37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]

# new_numbers = list(filter(lambda x: x < 47 or x > 47 and x % 2 == 0, numbers))
# new_numbers = list(map(lambda x: x // 2 if x % 2 == 0 else x, new_numbers))
# print(*new_numbers)
#
# # *************(В ОДНУ СТРОКУ)
# new_numbers = list(map(lambda y: y // 2 if y % 2 == 0 else y, filter(lambda x: x < 47 or x > 47 and x % 2 == 0, numbers)))
# print(*new_numbers)

# ***********(ОТ ПОЛЬЗОВАТЕЛЯ)
# print(*map(lambda x: [x // 2, x][x % 2], filter(lambda x: x < 48 or not x % 2, numbers)))
#[x % 2] дает либо 0, либо 1, соответственно, индекс выбирает из списка [x // 2, x] либо нулевое значение, либо первое
# Соответственно, если x четный, то дает 0 во второй скобке [x // 2, x][0] и, из первого списка берем выражение x // 2 по индексу 0.
# Если значение нечетное, то получаем [x // 2, x][1], которое забирает из первого списка просто х по индексу 1


# ***********(ОТ ПОЛЬЗОВАТЕЛЯ)
# print(*filter(None, map(lambda y: y//2 if y%2==0 else y if y<47 and y%2!=0 else None, numbers)))
#
# # *********(ОТ ПОЛЬЗОВАТЕЛЯ)(ЧЕРЕЗ ПОБИТОВЫЙ СДВИГ
# print(*map(lambda y: y >> (~y & 1), filter(lambda x: ~x & 1 or x < 48, numbers)))


# *************
# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'),
#         (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'),
#         (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
#
#
# filter_data = sorted(data, key=lambda x: x[1][-1], reverse=True)
# print(*map(lambda x: f'{x[1]}: {x[0]}', filter_data), sep='\n')
#
# # ***********(ОТ ПРЕПОДАВАТЕЛЯ)
# for pop, city in sorted(data, key=lambda x: x[1][-1], reverse=True):
#     print(f'{city}: {pop}')
#
# # **********(ОТ ПОЛЬЗОВАТЕЛЯ)(ЧЕРЕЗ СОЗДАНИЕ СЛОВАРЯ)
# a = sorted(data, key=lambda x: x[1][-1], reverse = True)
# d = dict(a)
# for key, value in d.items():
#     print(value, ': ', key, sep='')

# ***********
# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг',
#         'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид',
#         'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
#
# data_sort = sorted(data, key=lambda x: x)
# data_sort.sort(key=len)
# print(*data_sort)
#
# # **********(ОТ ПОЛЬЗОВАТЕЛЯ)(len(x), x) - это кортеж. Кортежи сравниваются во первым элементам, а если первые элементы равны - по вторым
# print(*sorted(data, key=lambda x: (len(x), x)))
#
# # **********(ОТ ПОЛЬЗОВАТЕЛЯ)
# data.sort()
# result = sorted(data, key=lambda x: len(x))
#
# print(*result)

# ***********
# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about',
#               454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434,
#               'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder',
#               1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot',
#               'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105,
#               'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish',
#               'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide',
#               'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022,
#               'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
#
#
# # result = max(filter(lambda x: type(x) is int, mixed_list))
# # print(result)
#
# # **********(ОТ ПОЛЬЗОВАТЕЛЯ)(ЧЕРЕЗ УСЛОВИЕ, ЧТО БЫ ПРОБЕЖАТЬ ВЕСЬ СПИСОК)
# result = max(mixed_list, key=lambda x: x if type(x) is int else 0)
# print(result)
#
# # *********(ОТ ПОЛЬЗОВАТЕЛЯ)(И ИСПОЛЬЗОВАНИЕМ КОРТЕЖА)
# print(max(mixed_list, key=lambda x: (isinstance(x, int), x)))


# *************
# mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday',
#               76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41,
#               'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80,
#               'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon',
#               'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt',
#               'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
#
# list_sort = sorted(mixed_list, key=lambda x: str(x))
# print(*list_sort)
#
# # *******(ОТ ПОЛЬЗОВАТЕЛЯ)(И ИСПОЛЬЗОВАНИЕМ КОРТЕЖА)
# print(*sorted(mixed_list, key=lambda x: (isinstance(x, str), x)))
#
# # *******(ОТ ПОЛЬЗОВАТЕЛЯ)(И ИСПОЛЬЗОВАНИЕМ СРАВНЕНИЯ КОРТЕЖА)
# print(*sorted(mixed_list, key=lambda x: (type(x) is str, x)))
#
# # **********(ОТ ПОЛЬЗОВАТЕЛЯ)
# print(*sorted(mixed_list, key=lambda x:(type(x).__name__, x)))


# ПРОТИВОПОЛОЖНЫЙ ЦВЕТ

# print(*list(map(lambda x: 255 - int(x), input().split())))
#
# # **********(ОТ ПОЛЬЗОВАТЕЛЯ)
# print(*map(int.__sub__, (255,) * 3, map(int, input().split())))
# __sub__ это магический метод (magic (or dunder - double-underscore) method) стоящий за опертором вычитания -.
# Поскольку для класса int определено вычитание, то можно сослатся на его магический метод в качестве аргумента
# функции map чтобы не расписывать lambda функцию. В качестве более универсальной альтернативы можно взять одноименные методы из модуля operator:


# ЗНАЧЕНИЕ МНОГОЧЛЕНА

# from functools import reduce
#
# def evaluate(cff, x):
#     indx = range(len(cff))[::-1]
#     lst = list(map(lambda num, i: int(num) * x ** i, cff, indx))
#     return reduce(lambda a, b: a + b, lst)
#
# n = input().split()
# x = int(input())
#
# print(evaluate(n, x))
#
# # ЗНАЧЕНИЕ МНОГОЧЛЕНА(ОТ ПОЛЬЗОВАТЕЛЯ)
# from functools import reduce as r
#
# evaluate = lambda coefficients, x: r(lambda v, c: c + v * x, map(int, coefficients))
# print(evaluate(input().split(), int(input())))

