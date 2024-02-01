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
# my_list = []
#
# for i in range(n + 1):
#     my_list.append(factorial(n) // (factorial(i) * factorial(n - i)))
#
# print(my_list)

# ТРЕУГОЛЬНИК ПАСКАЛЯ(ОТ ПОЛЬЗОВАТЕЛЯ)
# -------------------ФУНКЦИЯ-------------------
# def pascal(n):
#     triangle = [[1]]
#
#     for i in range(n):
#         row = [1]
#         for j in range(1, len(triangle[i])):
#             row += [sum(triangle[i][j - 1: j + 1])]
#         row += [1]
#         triangle.append(row.copy())
#
#     return triangle[n]


# --------------------ВЫЗОВ--------------------
# print(pascal(int(input())))


# ТРЕУГОЛЬНИК ПАСКАЛЯ(ОТ ПОЛЬЗОВАТЕЛЯ)
# def pascal(n):
#     # начальная строка
#     cur_seq = [1]
#
#     for _ in range(n):
#         # добавляем нули по бокам к текущей строке строке
#         cur_seq = [0] + cur_seq + [0]
#         # тут будет храниться новая строка
#         new_seq = []
#
#         for i in range(len(cur_seq) - 1):
#             # добавляем в новую строку сумму соседних элементов текущей строки
#             new_seq.append(cur_seq[i] + cur_seq[i + 1])
#
#         # теперь новая строка становится нашей текущей строкой
#         cur_seq = new_seq
#
#     return cur_seq
#
#
# n = int(input())
# print(pascal(n))



# ТРЕУГОЛЬНИК ПАСКАЛЯ 2

# def pascal(n):
#     # начальная строка
#     cur_seq = [1]
#
#     for _ in range(n):
#         print(*cur_seq)
#         # добавляем нули по бокам к текущей строке строке
#         cur_seq = [0] + cur_seq + [0]
#         # тут будет храниться новая строка
#         new_seq = []
#
#         for i in range(len(cur_seq) - 1):
#             # добавляем в новую строку сумму соседних элементов текущей строки
#             new_seq.append(cur_seq[i] + cur_seq[i + 1])
#
#         # теперь новая строка становится нашей текущей строкой
#         cur_seq = new_seq
#
#
# n = int(input())
# pascal(n)


# def pascal(n):
#     # результирующая таблица
#     seq = [[1]]
#     # начальная строка
#     cur_seq = [1]
#
#     for _ in range(n - 1):
#         # добавляем нули по бокам к текущей строке строке
#         cur_seq = [0] + cur_seq + [0]
#         # тут будет храниться новая строка
#         new_seq = []
#
#         for i in range(len(cur_seq) - 1):
#             # добавляем в новую строку сумму соседних элементов текущей строки
#             new_seq.append(cur_seq[i] + cur_seq[i + 1])
#
#         # теперь новая строка становится нашей текущей строкой
#         cur_seq = new_seq
#         # добавляем текущую строку в результирующую таблицу
#         seq.append(cur_seq)
#
#     return seq
#
#
# n = int(input())
# seq = pascal(n)
#
# # выводим таблицу по строкам
# for s in seq:
#     print(*s)


# УПАКОВКА ДУБЛИКАТОВ

# s = input().split()
#
# res = [[s[0]]]
#
# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         res[-1].append(s[i])
#     else:
#         res.append([s[i]])
#
# print(res)
#
# # УПАКОВКА ДУБЛИКАТОВ(ОТ ПРЕПОДАВАТЕЛЯ)
#
# s = input().split()
# # кидаем первый символ в наш список, также удалив его из входного списка
# seq = [[s.pop(0)]]
#
# for c in s:
#     if c in seq[-1]:
#         seq[-1].append(c)
#     else:
#         seq.append([c])
#
# print(seq)

# РАЗБИЕНИЕ НА ЧАНКИ

# def chunked(n, lst):
#     seq = []
#
#     for i in range(0, len(lst), n):
#         x = lst[i: i + n]
#         seq.append(x)
#
#     print(seq)
#
#
# symbols = input().split()
# n = int(input())
#
# chunked(n, symbols)
#
#
# # РАЗБИЕНИЕ НА ЧАНКИ(ОТ ПОЛЬЗОВАТЕЛЯ)
# def chunked(lst, n):
#     new = []
#     for i in range(len(lst)):
#         if i % n == 0:
#             new.append([lst[i]])
#         else:
#             new[-1].append(lst[i])
#     return new
#
# list_for_chunk = input().split()
# print(chunked(list_for_chunk, int(input())))

# РАЗБИЕНИЕ НА ЧАНКИ(ОТ ПОЛЬЗОВАТЕЛЯ)
# def chunked(x):
#     c, b = a, []
#     while c != []:
#         b.append(c[:x])
#         c = c[x:]
#     return b
#
# a = input().split()
# print(chunked(int(input())))






