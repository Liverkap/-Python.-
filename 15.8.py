
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


