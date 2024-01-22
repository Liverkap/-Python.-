
# СОДЕРЖИМОЕ ФАЙЛА

# file = open(input(), 'r', encoding='utf-8')
# content = file.read()
# print(content)
# file.close()

# СОДЕРЖИМОЕ ФАЙЛА(ОТ ПОЛЬЗОВАТЕЛЯ)
# file = open(input())
# print(file.read())
# file.close()
#
# # СОДЕРЖИМОЕ ФАЙЛА(ОТ ПОЛЬЗОВАТЕЛЯ)
# with open(input()) as f:
#     print(f.read())

# ПРЕДПОСЛЕДНЯЯ СТРОКА

# file = open(input(), 'r', encoding='utf-8')
# content = file.readlines()[-2]
#
# print(content)
# file.close()
#
# # ПРЕДПОСЛЕДНЯЯ СТРОКА(ОТ ПОЛЬЗОВАТЕЛЯ)
# name = input()
# file = open(name, 'r')
# print(list(file)[-2])
# file.close()

# СЛУЧАЙНАЯ СТРОКА
# import random
#
# file = open('lines.txt', 'r', encoding='utf-8')
# content = file.readlines()
# print(content[random.randint(0, len(content) - 1)])
# file.close()

# СЛУЧАЙНАЯ СТРОКА(ОТ ПОЛЬЗОВАТЕЛЯ)
# import random
# file = open('lines.txt')
# print(random.choice(file.readlines()))
# file.close
#
# # СЛУЧАЙНАЯ СТРОКА(ОТ ПОЛЬЗОВАТЕЛЯ)
# from random import randrange
# file = open('lines.txt', 'r', encoding='utf-8')
# text = list(file)
# print(text[randrange(len(text))])
# file.close()


# СУММА ДВУХ-1

# file = open('numbers.txt', 'r', encoding='utf-8')
#
# content = [int(num.rstrip()) for num in list(file)]
# print(sum(content))
# file.close()

# СУММА ДВУХ-1(ОТ ПРЕПОДАВАТЕЛЯ)
# file = open('numbers.txt')
#
# print(sum(map(int, file)))
#
# file.close()


# СУММА ДВУХ-2

# file = open('nums.txt', 'r', encoding='utf-8')
#
# res = sum(map(int, file.read().split()))
#
# print(res)
# file.close()


# ОБЩАЯ СТОИМОСТЬ

# file = open('prices.txt', 'r', encoding='utf-8')
#
# res = sum(map(lambda x: int(x[1]) * int(x[2]), map(lambda x: x.replace('\t', ' ').rstrip('\n').split(), file)))
# print(res)
#
# file.close()
#
# # ОБЩАЯ СТОИМОСТЬ(ОТ ПОЛЬЗОВАТЕЛЯ)
# file = open('prices.txt')
# lines = map(str.split, file)
# print(sum(map(lambda line: int(line[1]) * int(line[2]), lines)))
# file.close()
#
#
# # ОБЩАЯ СТОИМОСТЬ(ОТ ПОЛЬЗОВАТЕЛЯ)
# file = open('prices.txt', 'r', encoding='utf-8')
# s = 0
# for line in file:
#     tovar, count, price = line.split()
#     s += int(count) * int(price)
# print(s)
# file.close()


# ОБЩАЯ СТОИМОСТЬ(ОТ МЕНЯ)

# file = open('prices.txt', 'r', encoding='utf-8')
#
# content = [int(count) * int(price) for name, count, price in map(str.split, file)]
#
# print(sum(content))
#
# file.close()


# ОБЩАЯ СТОИМОСТЬ(ОТ ПОЛЬЗОВАТЕЛЯ)
# from functools import reduce
#
# file = open("prices.txt", encoding="utf-8")
# prods = [ x.split() for x in file.readlines()]
# amount = reduce(lambda a,b:  a + int(b[1]) * int(b[2]), prods, 0)
# print(amount)
# file.close()

