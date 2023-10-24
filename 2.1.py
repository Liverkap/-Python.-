# НА EASY

# a, b = int(input()), int(input())
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print((a ** 10 + b ** 10) ** 0.5)

# НА EASY (ОТ ПОЛЬЗОВАТЕЛЯ)

# a, b = int(input()), int(input())
#
# for i in [a + b, a - b, a * b, a / b, a // b, a % b, (a ** 10 + b ** 10) ** 0.5]:
#     print(i)


# ИНДЕКСЫ МАССЫ ТЕЛА

# def find_body_mass_index(weight, hight):
#     return weight / hight ** 2
#
# weight, hight = float(input()), float(input())
#
# imt = find_body_mass_index(weight, hight)
#
# if imt < 18.5:
#     print('Недостаточная масса')
# elif imt > 25:
#     print('Избыточная масса')
# else:
#     print('Оптимальная масса')


# СТОИМОСТЬ СТРОКИ

# def count_price_string(s):
#     total_price = 0
#     for _ in range(len(s)):
#         total_price += 60
#
#     return f'{total_price // 100} р. {total_price % 100} коп.'
#
# string = input()
# print(count_price_string(string))
#
#
#
# # СТОИМОСТЬ СТРОКИ (ОТ ПРЕПОДАВАТЕЛЯ)
# string = input()
# price = 60 * len(string)
#
# print(f'{price // 100} р. {price % 100} коп.')


# КОЛИЧЕСТВО СЛОВ

# string = input().split()
#
# print(len(string))


# ЗОДИАК

# zodiac = ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца']
#
# year = int(input())
#
# print(zodiac[year % 12])
#
#
# # ЗОДИАК (ОТ ПОЛЬЗОВАТЕЛЯ)
#
# s = ['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц',]
# print(s[(int(input()) - 2000) % 12])


# ПЕРЕВОРОТ ЧИСЛА

# n = int(input())
#
# if len(str(n)) == 5:
#     print(int(str(n)[::-1]))
# else:
#     reversed_s = ''.join(reversed(str(n)[1:]))
#     print(int(str(n)[:1] + reversed_s))
#
#
# # ПЕРЕВОРОТ ЧИСЛА (ОТ ПРЕПОДАВАТЕЛЯ)
# n = input()
# new_n = int(n[:-5] + n[-5:][::-1])
#
# print(new_n)


# STANDART AMERICAN CONVENTION

# def add_comma(num):
#     if num < 999:
#         return num
#


# n = 1000000
# my_list = []
# for i in range(len(str(n))):
#     my_list.append(str(n)[i])
#
# print(my_list)
# my_list.reverse()
# # print(my_list)
# # print(sec_list)
# for _ in range(0, len(str(n)), 3):
#     my_list.append(',')
# print(my_list)
# n = int(input())
# my_list = []
#
# for c in str(n):
#     my_list.append(c)
#
# if 1000 <= n <= 9999:
#     my_list.insert(1, ',')
#

#
# print(*my_list, sep='')
# # x = str(n).split()
# # print(x)
# # if 1000 <= n <= 9999:
# #     x.insert(2, ',')
# # print(*x)

# print(10 **100)