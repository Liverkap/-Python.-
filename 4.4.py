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


# СЛЕД МАТРИЦЫ
# Следом квадратной матрицы называется сумма элементов главной диагонали


# n = int(input())
# matrix = []
#
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
#
# total = 0
#
# for i in range(n):
#     total += matrix[i][i]
#
# print(total)


# СЛЕД МАТРИЦЫ (ОТ ПРЕПОДАВАТЕЛЯ)

# n = int(input())
#
# sm = 0
#
# for i in range(n):
#     cur_seq = input().split()
#     sm += int(cur_seq[i])
#

# # СЛЕД МАТРИЦЫ (ОТ ПОЛЬЗОВАТЕЛЯ)
# res = 0
# for i in range(int(input())):
#     res += int(input().split()[i])
# print(res)


# БОЛЬШЕ СРЕДНЕГО

# n = int(input())
#
# matrix = []
#
# for _ in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
#
#
# for i in range(n):
#     seq = sum(matrix[i]) / len(matrix[i])
#     count = 0
#     for j in range(n):
#         if matrix[i][j] > seq:
#             count += 1
#     print(count)

# БОЛЬШЕ СРЕДНЕГО (С СОЗДАНИЕМ ФУНКЦИИ СОЗДАНИЯ МАТРИЦЫ)
# def create_matrix(n):
#     matrix = [[int(num) for num in input().split()] for _ in range(n)]
#     return matrix
#
#
# n = int(input())
# my_matrix = create_matrix(n)
#
# for i in range(n):
#     seq = sum(my_matrix[i]) / len(my_matrix[i])
#     count = 0
#     for j in range(n):
#         if my_matrix[i][j] > seq:
#             count += 1
#     print(count)


# МАКСИМАЛЬНЫЙ В ОБЛАСТИ 1

# def create_matrix(n):
#     matrix = [[int(num) for num in input().split()] for _ in range(n)]
#     return matrix
#
# n = int(input())
# my_matrix = create_matrix(n)
#
# maximum = -1000
#
# for i in range(n):
#     for j in range(n):
#         if (i >= j and i <= n - 1 - j) or (i >= j and i >= n - 1 - j):
#             if my_matrix[i][j] > maximum:
#                 maximum = my_matrix[i][j]
#
# print(maximum)

# МАКСИМАЛЬНЫЙ В ОБЛАСТИ 1 (ОТ ПРЕПОДАВАТЕЛЯ)

# n = int(input())
# matrix = []
#
# for _ in range(n):
#     row = [int(i) for i in input().split()]
#     matrix.append(row)
#
# largest = matrix[0][0]
#
# for i in range(n):
#     for j in range(n):
#         if i >= j and matrix[i][j] > largest:
#             largest = matrix[i][j]
#
# print(largest)


# МАКСИМАЛЬНЫЙ В ОБЛАСТИ 2

# def create_matrix(n):
#     matrix = [[int(num) for num in input().split()] for _ in range(n)]
#     return matrix
#
# n = int(input())
# my_matrix = create_matrix(n)
#
# maximum = my_matrix[0][0]
#
# for i in range(n):
#     for j in range(n):
#         if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j):
#             if my_matrix[i][j] > maximum:
#                 maximum = my_matrix[i][j]
#
# print(maximum)


# СУММЫ ЧЕТВЕРТЕЙ

# def create_matrix(n):
#     matrix = [[int(num) for num in input().split()] for _ in range(n)]
#     return matrix
#
# n = int(input())
# my_matrix = create_matrix(n)
#
# up_quater = 0
# right_quater = 0
# down_quater = 0
# left_quater = 0
#
# for i in range(n):
#     for j in range(n):
#         if i > j and i < n - 1 - j:
#             left_quater += my_matrix[i][j]
#         elif i > j and i > n - 1 - j:
#             down_quater += my_matrix[i][j]
#         elif i < j and i > n - 1 - j:
#             right_quater += my_matrix[i][j]
#         elif i < j and i < n - 1 - j:
#             up_quater += my_matrix[i][j]
#
# print(f'Верхняя четверть: {up_quater}')
# print(f'Правая четверть: {right_quater}')
# print(f'Нижняя четверть: {down_quater}')
# print(f'Левая четверть: {left_quater}')


# СУММЫ ЧЕТВЕРТЕЙ (ОТ ПРЕПОДАВАТЕЛЯ)
# n = int(input())
# matrix = []
# quadrants = [['Верхняя четверть:', 0],
#              ['Правая четверть:', 0],
#              ['Нижняя четверть:', 0],
#              ['Левая четверть:', 0]]
#
# for _ in range(n):
#     row = [int(i) for i in input().split()]
#     matrix.append(row)
#
# for i in range(n):
#     for j in range(n):
#         if i < j and i + j + 1 < n :
#             quadrants[0][1] += matrix[i][j]
#         elif i < j and i + j + 1 > n:
#             quadrants[1][1] += matrix[i][j]
#         elif i > j and i + j + 1 > n:
#             quadrants[2][1] += matrix[i][j]
#         elif i > j and i + j + 1 < n:
#             quadrants[3][1] += matrix[i][j]
#
# for i in range(4):
#     print(quadrants[i][0], quadrants[i][1])