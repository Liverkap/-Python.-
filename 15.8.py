
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


