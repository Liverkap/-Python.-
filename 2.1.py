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