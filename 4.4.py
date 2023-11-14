# Матрица m на n
# где m - строки, n - столбцы


# matrix  = [[2, -5, -11, 0],
#            [-9, 4, 6, 13],
#            [4, 7, 12, -2]]
#
# print(matrix[1][2])



# ПЕРЕБОР ЭЛЕМЕНТОВ МАТРИЦЫ
# Чтобы перебрать элементы матрицы, необходимо использовать вложенные циклы


# rows, cols = 3, 4  # rows - количество строк, cols - количество столбцов
#
# matrix = [[2, 3, 1, 0],
#            [9, 4, 6, 8],
#            [4, 7, 2, 7]]
#
# for r in range(rows):
#     for c in range(cols):
#         print(matrix[r][c], end=' ')
#     print()


# Для перебора элементов матрицы по столбцам можно использовать следующий код

# rows, cols = 3, 4  # rows - количество строк, cols - количество столбцов
#
# matrix = [[2, 3, 1, 0],
#            [9, 4, 6, 8],
#            [4, 7, 2, 7]]
#
# for c in range(cols):
#     for r in range(rows):
#         print(matrix[r][c], end=' ')
#     print()


#       ****************** Функции ljust() и rjust()    *********
# Метод ljust() - Строковый метод ljust() выравнивает текст по ширине, добавляя пробелы в конец текста
# print('a'.ljust(3))
# print('ab'.ljust(3))
# print('abc'.ljust(3))
#
# # Строковый метод ljust() использует вместо пробела другой символ, если передать ему второй аргумент, необязательный.
# print('a'.ljust(5, '*'))
# print('ab'.ljust(5, '$'))
# print('abc'.ljust(5, '#'))
#
#
# # Метод rjust() - Строковый метод rjust() выравнивает текст по ширине, добавляя пробелы в начало текста
#
# print('a'.rjust(3))
# print('ab'.rjust(3))
# print('abc'.rjust(3))
#
# # Строковый метод rjust() использует вместо пробела другой символ, если передать ему второй аргумент, необязательный.
#
# print('a'.rjust(5, '*'))
# print('ab'.rjust(5, '$'))
# print('abc'.rjust(5, '#'))
#
#
# rows, cols = 3, 4  # rows - количество строк, cols - количество столбцов
#
# matrix  = [[277, -930, 11, 0],
#            [9, 43, 6, 87],
#            [4456, 8, 290, 7]]
#
# for r in range(rows):
#     for c in range(cols):
#         print(str(matrix[r][c]).ljust(6), end='')
#     print()


#       ***************************** КВАДРАТНЫЕ МАТРИЦЫ    ***********************

# Матрица с одинаковым количеством строк и столбцов называется квадратной. У квадратной матрицы есть две диагонали

# главная: проходит из верхнего левого в правый нижний угол матрицы;
# побочная: проходит из нижнего левого в правый верхний угол матрицы.


# Элементы с равными индексами i == j находятся на главной диагонали. Такие элементы обозначаются matrix[i][i]
# Элементы с индексами i и j, связанными соотношением i + j + 1 = n (или j = n - i - 1), где n — размерность матрицы, находятся на побочной диагонали.

# Чтобы установить элементы главной или побочной диагонали, достаточно одного цикла

# n = 8
# matrix = [[0] * n for _ in range(n)] # создаем квадратную матрицу размером 8×8
#
# for i in range(n):  # заполняем главную диагональ единицами, а побочную двойками
#     matrix[i][i] = 1
#     matrix[i][n - i - 1] = 2
#     print(matrix)
#
# for r in range(n):
#     for c in range(n):
#         print(matrix[r][c], end=' ')
#     print()

# если элемент находится выше главной диагонали, то i < j, если ниже - i > j.
# если элемент находится выше побочной диагонали, то i + j + 1 < n, если ниже - i + j + 1 > n.


# Примечание 2. Используйте функцию print_matrix() для вывода квадратной матрицы размерности n:
# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()


# Примечание 3. Для считывания матрицы из n строк, заполненной числами, удобно использовать следующий код:
# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# print(matrix)


# матрицу можно создать с помощью   генератора:!!!!!!!
#
# [[input() for _ in range(m)] for _ in range(n)]


# n = 5
# a = [[19, 21, 33, 78, 99],
#      [41, 53, 66, 98, 76],
#      [79, 80, 90, 60, 20],
#      [33, 11, 45, 67, 90],
#      [45, 67, 12, 98, 23]]
#
# maximum = -1
# minimum = 100
#
# for i in range(n):
#     if a[i][i] > maximum:
#         maximum = a[i][i]
#     if a[i][n - i - 1] < minimum:
#         minimum = a[i][n - i - 1]
#
# print(minimum + maximum)


# ВЫВЕСТИ МАТРИЦУ 1

# n, m = int(input()), int(input())
#
# matrix = [[input() for _ in range(m)] for _ in range(n)]
#
# for r in range(n):
#     for c in range(m):
#         print(matrix[r][c], end=' ')
#     print()
#
# # ВЫВЕСТИ МАТРИЦУ 1 (ОТ ПРЕПОДАВАТЕЛЯ)(ДЛИННОЕ РЕШЕНИЕ)
# n, m = int(input()), int(input())
# matrix = []
#
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(input())
#     matrix.append(row)
#
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end=' ')
#     print()

# ВЫВЕСТИ МАТРИЦУ 1 (ОТ ПРЕПОДАВАТЕЛЯ)(КОРОТКОЕ РЕШЕНИЕ)

# n, m = int(input()), int(input())
# matrix = [[input() for _ in range(m)] for _ in range(n)]
#
# for row in matrix:
#     print(*row)


# ВЫВЕСТИ МАТРИЦУ 2

# n, m = int(input()), int(input())
#
# matrix = [[input() for _ in range(m)] for _ in range(n)]
#
# for row in matrix:
#     print(*row)
#
# print()
#
# for i in range(m):
#     for j in range(n):
#         print(matrix[j][i], end=' ')
#     print()
#
# # ВЫВЕСТИ МАТРИЦУ 2 (ОТ ПРЕПОДАВАТЕЛЯ)
#
# n, m = int(input()), int(input())
# matrix = []
#
# for _ in range(n):
#     row = [input() for j in range(m)]
#     matrix.append(row)
#
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end=' ')
#     print()
#
# print()
#
# for j in range(m):
#     for i in range(n):
#         print(matrix[i][j], end=' ')
#     print()