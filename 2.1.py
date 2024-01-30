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

# ПЕРЕВОРОТ ЧИСЛА (ОТ ПОЛЬЗОВАТЕЛЯ) (в 2 строки)
# s = input()
# print(int(s[:-5] + s[-1:-6:-1]))


# STANDART AMERICAN CONVENTION


# print('{:,}'.format(int(input())))


# STANDART AMERICAN CONVENTION (ОТ ПРЕПОДАВАТЕЛЯ)

# seq = list(input())
#
# new_s = ''
#
# while len(seq) >= 3:
#     new_s += seq.pop(-1) + seq.pop(-1) + seq.pop(-1) + ','
#
# new_s += ''.join(seq[::-1])
#
# new_s = new_s[::-1]
# new_s = new_s.lstrip(',')
#
# print(new_s)


# ЗАДАЧА ИОСИФА ФЛАВЕЛЯ

# n, k = int(input()), int(input())
#
# new_list = list(range(1, n + 1))
#
# while len(new_list) > 1:
#     for _ in range(1, k):
#         temp = new_list.pop(0)
#         new_list.append(temp)
#     new_list.pop(0)
#
# print(*new_list)


# ЗАДАЧА ИОСИФА ФЛАВЕЛЯ(ОТ ПРЕПОДАВАТЕЛЯ)
# n = int(input())
# k = int(input())
#
# res = 0
# for i in range(1, n + 1):
#     res = (res + k) % i
# print(res + 1)

# ЗАДАЧА ИОСИФА ФЛАВЕЛЯ(ОТ ПОЛЬЗОВАТЕЛЯ)
# def joseph(n, k):
#     return 1 if n == 1 else (joseph(n - 1, k) + k - 1) % n + 1
#
# print(joseph(int(input()), int(input())))



