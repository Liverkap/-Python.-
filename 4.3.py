#               *********************   ВАРИАНТЫ СОЗДАНИЯ СПИСКОВ   ***********

# ПЕРВЫЙ СПОСОБ

# n, m = int(input()), int(input())
#
# my_list = []
#
# for _ in range(n):
#     my_list.append([0] * m)
#
# print(my_list)

# ВТОРОЙ СПОСОБ

# n, m = int(input()), int(input())
#
# my_list = [0] * n
#
# for i in range(n):
#     my_list[i] = [0] * m
#
# print(my_list)


# ТРЕТИЙ СПОСОБ (ЧЕРЕЗ ГЕНЕРАТОР СПИСКА)

# n, m = int(input()), int(input())
#
# my_list = [[0] * m for _ in range(n)]
#
# print(my_list)

# СЧИТЫВАЕНИЕ ВЛОЖЕННЫХ СПИСКОВ
# n = 4                                         # количество строк (элементов)
# my_list = []
#
# for _ in range(n):
#     elem = [int(i) for i in input().split()]  # создаем список из элементов строки
#     my_list.append(elem)
#
# print(my_list)

# ПЕРЕБОР И ВЫВОД

# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print(my_list[i][j], end=' ')  # используем необязательный параметр end
#     print()                            # перенос на новую строку


# МОЖНО ПЕРЕБИРАТЬ САМИ ЭЛЕМЕНТЫ ВЛОЖЕННЫХ СПИСКОВ (БЕЗ ИНДЕКСОВ)

# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for row in my_list:
#     for elem in row:
#         print(elem, end=' ')
#     print()


#       *** ОБРАБОТКА ВЛОЖЕННЫХ ЦИКЛОВ  ******

# my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
#
# total = 0
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         total += my_list[i][j]
#
# print(total)


# my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
#
# total = 0
# for row in my_list:
#     for elem in row:
#         total += elem
#
# print(total)

# ПОДСЧЕТ С ПОМОЩЬЮ ФУНКЦИИ SUM
# my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
#
# total = 0
# for row in my_list:  # в один цикл
#     total += sum(row)
# print(total)


# list1 = [[1, 2, 3], [4, 5]]
# list2 = list1
#
# list1[0].append(7)
#
# print(list2)


# n, m = int(input()), int(input())
#
# my_list = [[1] * m] * n
# my_list[0][1] = 5
# print(my_list)


# СПИСОК ПО ОБРАЗЦУ

# n = int(input())
#
# for _ in range(n):
#     my_list = []
#     for i in range(1, n + 1):
#         my_list.append(i)
#     print(my_list)


# СПИСОК ПО ОБРАЗЦУ (ОТ ПРЕПОДАВАТЕЛЯ)

# n = int(input())
# result = []
#
# for _ in range(n):
#     result.append(list(range(1, n + 1)))
#
# print(*result, sep='\n')


# СПИСОК ПО ОБРАЗЦУ (ОТ ПОЛЬЗОВАТЕЛЯ)
# n=int(input())
# my_list=[[i for i in range(1,n+1)] for i in range(n)]
# for row in my_list:
#     print(row)


# СПИСОК ПО ОБРАЗЦУ 2

# n = int(input())
#
#
# for i in range(1, n + 1):
#     my_list = []
#     for j in range(1, i + 1):
#         my_list.append(j)
#     print(my_list)

# СПИСОК ПО ОБРАЗЦУ 2 (ОТ ПРЕПОДАВАТЕЛЯ)

# n = int(input())
# result = []
#
# for i in range(1, n + 1):
#     result.append(list(range(1, i + 1)))
#
# print(*result, sep='\n')

# СПИСОК ПО ОБРАЗЦУ 2 (ОТ ПОЛЬЗОВАТЕЛЯ)
# n = int(input())
# for j in range(1, n+1):
#     print([i for i in range(1, j+1)])


# ТРЕУГОЛЬНИК ПАСКАЛЯ



# from math import factorial
# n = int(input())
#
# my_list = [1] * (n + 1)
#
#
# for i in range(1, n):
# # for j in range(i):
#     my_list[i] = factorial(n) // (factorial(my_list[i]) * factorial(n - my_list[i]))
#
# print(my_list)


# ТРЕУГОЛЬНИК ПАСКАЛЯ 2

# n = int(input())
#
# my_list = []
#
# for i in range(n):
#     new_list = []
#     for j in range(i + 1):
#         new_list.append(i)
#         my_list.append(new_list)
#     print(my_list)


# УПАКОВКА ДУБЛИКАТОВ

# s = input().split()
#
# print(s)
# my_list = []
#
# for i in range(len(s)):
#     my_list.append([s[i]])
#
# print(my_list)


# s = [[i] for i in range(len(input().split()))]
#
# s = [[c] for c in input().split()]
#
# my_list = []
#
# for i in range(len(s)):
#     if s[i] == s[i + 1]:
#         my_list[i] = s[i + 1]
#
#
# print(s)