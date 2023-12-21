#               *****   МОДУЛЬ RANDOM   *************
# import random
#               *******     Метод shuffle()     *************
# Метод shuffle() принимает список в качестве обязательного аргумента и перемешивает его случайным образом.

# import random
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# random.shuffle(numbers)
# print(numbers)


#               *****************       Метод choice()      ****************
# Метод choice() принимает список (строку, кортеж) в качестве обязательного аргумента и возвращает один случайный элемент.

# import random
#
# print(random.choice('BEEGEEK'))
# print(random.choice([1, 2, 3, 4]))
# print(random.choice(('a', 'b', 'c', 'd')))

# *************
# import random
#
# for _ in range(15):
#     print(random.choice('abcdefghijklmnoppq'))


#           *********************       Метод sample()      **********

# Метод sample() принимает два обязательных аргумента: первый – список (строка, кортеж, множество),
# второй – количество случайных элементов. Возвращает список из указанного количества уникальных (имеющих разные индексы) случайных элементов.

# import random
#
# numbers = [2, 5, 8, 9, 12]
#
# print(random.sample(numbers, 1))
# print(random.sample(numbers, 2))
# print(random.sample(numbers, 3))
# print(random.sample(numbers, 5))

# Количество случайных элементов не должно превышать длину исходного списка (строки)


#                   ********************        Модуль string       *********

# Встроенный модуль string раньше использовался для расширения стандартных возможностей (функционала)
# строкового типа данных str. На текущий момент все функции из модуля string переехали в методы строкового типа данных
# str, однако в модуле string остались удобные константные строки, которые можно использовать при решении задач.

# import string
#
# print(string.ascii_letters)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.octdigits)
# print(string.punctuation)
# print(string.printable)


# *******
# import random
# def generate_ip():
#     my_list = []
#     for _ in range(4):
#         x = random.randint(0, 255)
#         my_list.append(str(x))
#
#     return '.'.join(my_list)
#
# print(generate_ip())

# ********** (ОТ ПРЕПОДАВАТЕЛЯ)
# from random import randrange as r
#
# def generate_ip():
#     return f'{r(256)}.{r(256)}.{r(256)}.{r(256)}'
#
# print(generate_ip())

# ***************
# import random
# import string
#
# def generate_index():
#     letters = string.ascii_uppercase
#     numbers = string.digits
#     index = []
#     index.extend(random.sample(letters, 2))
#     index.extend(random.sample(numbers, 4))
#     index.extend(random.sample(letters, 2))
#     index = ''.join(index)
#
#     return f'{index[:4]}_{index[4:]}'
#
#
# print(generate_index())


# ************(ОТ ПОЛЬЗОВАТЕЛЯ)

# from random import choice, randint
# from string import ascii_uppercase as letter
#
# def generate_index():
#     return f'{choice(letter)}{choice(letter)}{randint(0, 99)}_{randint(0, 99)}{choice(letter)}{choice(letter)}'
#
# print(generate_index())

# ************(ОТ ПОЛЬЗОВАТЕЛЯ)
# from random import randint, choice
# from string import ascii_uppercase as letters
# def generate_index():
#     def r_char():
#         return choice(letters)
#     def r_digit():
#         return str(randint(0,99))
#     result = r_char() + r_char() + r_digit() + '_' + r_digit() + r_char() + r_char()
#     return result


# *************
# import random
#
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# for i in range(len(matrix)):
#     x = matrix.pop(0)
#     random.shuffle(x)
#     matrix.append(x)
#
# print(matrix)

# ***************(ОТ ПОЛЬЗОВАТЕЛЯ)(БЕЗ УДАЛЕНИЯ ЭЛЕМЕНТОВ)
# import random
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# for el in matrix:
#     random.shuffle(el)


# sum(matrix, []) превращает матрицу в одномерный список, значения которого затем тусуются методом shuffle. Потом из одномерного массива опять строится матрица.


# ************
# import random as rnd
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# n, m, lst = len(matrix), len(matrix[0]), sum(matrix, [])
# rnd.shuffle(lst)
# matrix = [[lst[i * m + j] for j in range(m)] for i in range(n)]
#
# print(matrix)


# **************

# import random
# from string import digits
#
# count = 0
#
# while count != 100:
#     ticket_old = random.sample(list(digits), 7)
#     ticket = ''
#     for i in range(7):
#         ticket += random.choice(digits)
#     if ticket.startswith('0') or ticket == ticket_old:
#         continue
#     ticket_old = ticket
#     print(ticket)
#     count += 1


# ********(ОТ ПОЛЬЗОВАТЕЛЯ)(КОРОТКИЙ КОД ЧЕРЕЗ СОЗДАНИЕ МНОЖЕСТВ)
# from random import randint
# s = set()
# while len(s) != 100:
#     s.add(randint(1000000, 9999999))
# print(*s, sep='\n')
#
#
# # ********(ОТ ПОЛЬЗОВАТЕЛЯ)(КОРОТКИЙ КОД ЧЕРЕЗ SAMPLE)(SAMPLE СОЗДАЕТ УНИКАЛЬНЫЕ ЧИСЛА)
# from random import sample as r
#
# print(*r(range(int(1e6), int(1e7)), 100), sep='\n')


# *************
# from random import shuffle as shfl
#
# word = input()
#
# annagram = []
#
# for ch in word:
#     annagram.append(ch)
#
# shfl(annagram)
# print(''.join(annagram))

# *******(ОТ ПОЛЬЗОВАТЕЛЯ)
# import random as r
# w = list(input())
# r.shuffle(w)
# print(*w, sep='')

# ********(ОТ ПОЛЬЗОВАТЕЛЯ)
# import random
# a = list(input())
# random.shuffle(a)
# print(''.join(a))

# ************БИНГО
# import random
#
# numbers = list(range(1, 76))
#
# num_line = random.sample(numbers, 25)
#
# bingo = [[str(num_line.pop()).ljust(3) for _ in range(5)] for _ in range(5)]
#
# bingo[2][2] = str(0).ljust(3)
#
# [print(*row, sep='') for row in bingo]


# ************БИНГО (ОТ ПРЕПОДАВАТЕЛЯ)
# from random import sample
#
# numbers = sample(list(range(1, 76)), 25)
# bingo = [numbers[i:i + 5] for i in range(0, 21, 5)]
# bingo[2][2] = 0
#
# for i in range(5):
#     for j in range(5):
#         print(str(bingo[i][j]).ljust(3), end=' ')
#     print()













