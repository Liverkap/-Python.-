# ТАБЛИЦА УМНОЖЕНИЯ

# n, m = int(input()), int(input())
#
# mult = []
#
# for i in range(n):
#     temp = []
#     for j in range(m):
#         temp.append(i * j)
#     mult.append(temp)
#
# for i in range(n):
#     for j in range(m):
#         print(str(mult[i][j]).ljust(3), end='')
#     print()

# ТАБЛИЦА УМНОЖЕНИЯ (ВАРИАНТ 2)

# n, m = int(input()), int(input())
#
# mult = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         mult[i][j] = i * j
#
# for i in range(n):
#     for j in range(m):
#         print(str(mult[i][j]).ljust(3), end=' ')
#     print()


# МАКСИМУМ В ТАБЛИЦЕ
# def create_matrix(n):
#     matrix = [[int(num) for num in input().split()] for _ in range(n)]
#     return matrix
#
# n, m = int(input()), int(input())
# my_matrix = create_matrix(n)
#
# largest = my_matrix[0][0]
# index_i = 0
# index_j = 0
# for i in range(n):
#     for j in range(m):
#         if my_matrix[i][j] > largest:
#             largest = my_matrix[i][j]
#             index_i = i
#             index_j = j
#
# print(index_i, index_j)
#
# # МАКСИМУМ В ТАБЛИЦЕ (ОТ ПРЕПОДАВАТЕЛЯ)
#
# n, m = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# row, col = 0, 0
#
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > matrix[row][col]:
#             row, col = i, j
#
# print(row, col)


# ОБМЕН СТОЛБЦОВ

# def create_matrix(n):
#     matrix = [[int(num) for num in input().split()] for _ in range(n)]
#     return matrix
#
# n, m = int(input()), int(input())
# my_matrix = create_matrix(n)
#
# index_i, index_j = [int(num) for num in input().split()]
#
# for i in range(n):
#     for j in range(m):
#         if j == index_j:
#             num_i = my_matrix[i][index_j]
#             num_j = my_matrix[i][index_i]
#             my_matrix[i][index_i] = num_i
#             my_matrix[i][index_j] = num_j
#
# for i in range(n):
#     for j in range(m):
#         print(my_matrix[i][j], end=' ')
#     print()


# ОБМЕН СТОЛБЦОВ (ОТ ПРЕПОДАВАТЕЛЯ)

# n, m = int(input()), int(input())
# matrix = [input().split() for _ in range(n)]
# col1, col2 = [int(i) for i in input().split()]
#
# for i in range(n):
#     matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]
#
# for row in matrix:
#     print(*row)


# СИММЕТРИЧНАЯ МАТРИЦА

# def create_matrix(n):
#     matrix = [[int(num) for num in input().split()] for _ in range(n)]
#     return matrix
#
# n = int(input())
#
# my_matrix = create_matrix(n)
#
# flag = True
# for i in range(n):
#     for j in range(n):
#         if i != j:
#             if my_matrix[i][j] != my_matrix[j][i]:
#                 flag = False
#                 break
#     if flag is False:
#         break
#
# if flag:
#     print('YES')
# else:
#     print('NO')


# СИММЕТРИЧНАЯ МАТРИЦА (ОТ ПРЕПОДАВАТЕЛЯ)

# n = int(input())
# matrix = [input().split() for _ in range(n)]
# result = 'YES'
#
# for i in range(n):
#     for j in range(i + 1, n):
#         if matrix[i][j] != matrix[j][i]:
#             result = 'NO'
#             break
#     if result == 'NO':
#         break
#
# print(result)


# ОБМЕН ДИАГОНАЛЯМИ


# def create_matrix(n):
#     matrix = [[int(num) for num in input().split()] for _ in range(n)]
#     return matrix
#
# n = int(input())
#
# my_matrix = create_matrix(n)
#
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             a = my_matrix[i][j]
#             b = my_matrix[n-i-1][i]
#             my_matrix[i][j] = b
#             my_matrix[n-i-1][i] = a
#
# for el in my_matrix:
#     print(*el)

# ОБМЕН ДИАГОНАЛЯМИ (ОТ ПРЕПОДАВАТЕЛЯ)


# n = int(input())
# matrix = [input().split() for _ in range(n)]
#
# for i in range(n):
#     matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]
#
# for row in matrix:
#     print(*row)


# ЗЕРКАЛЬНОЕ ОТОБРАЖЕНИЕ

# n = int(input())
# matrix = [input().split() for _ in range(n)]
#
# for i in range(n // 2):
#     matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]
#
# for el in matrix:
#     print(*el)

# ПОВОРОТ МАТРИЦЫ

# n = int(input())
# matrix = [input().split() for _ in range(n)]
#
# matrix.reverse()
#
# for i in range(n):
#     for j in range(n):
#         print(matrix[j][i], end=' ')
#     print()

# ПОВОРОТ МАТРИЦЫ (ОТ ПРЕПОДАВАТЕЛЯ)
# n = int(input())
# matrix = [input().split() for _ in range(n)]
# result = [[0] * n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         result[i][j] = matrix[n - j - 1][i]
#
# for row in result:
#     print(*row)

# ПОВОРОТ МАТРИЦЫ (ОТ ПОЛЬЗОВАТЕЛЯ)
# matrix = []
#
# for _ in range(int(input())):
#     matrix.append([int(x) for x in input().split()])
#
# for row in zip(*matrix[::-1]):
#     print(*row)

# ПОВОРОТ МАТРИЦЫ (ОТ ПОЛЬЗОВАТЕЛЯ)
# n = int(input())
# a = [input().split() for _ in range(n)]
# [print(*[a[n-j-1][i] for j in range(n)]) for i in range(n)]


# ХОДЫ КОНЯ

# def knight(n):
#     x = 8 - int(n[1])
#     y = ord(n[0]) - 97
#     mx = [['.'] * 8 for i in range(8)]
#     for i in range(8):
#         for j in range(8):
#             if abs(x - i) == 2 and abs(y - j) == 1 or abs(x - i) == 1 and abs(y - j) == 2:
#                 mx[i][j] = '*'
#             mx[x][y] = 'N'
#     for i in mx:
#         print(*i, end=' ')
#         print()
#
# knight(input())


# МАГИЧЕСКИЙ КВАДРАТ

# n = int(input())
# numbers = list(range(1, n ** 2 + 1))
# matrix = [[int(num) for num in input().split() ] for _ in range(n)]
#
# res = {}
# check_list = []
#
# for i in range(n):
#     res['main_diagonal'] = res.setdefault('main_diagonal', 0) + int(matrix[i][i])
#     res['side_diagonal'] = res.setdefault('side_diagonal', 0) + int(matrix[i][n - i - 1])
#     for j in range(n):
#         check_list.append(matrix[i][j])
#         res[f'sum_row_{i+1}'] = res.setdefault(f'sum_row_{i+1}', 0) + int(matrix[i][j])
#         res[f'sum_colomn_{j+1}'] = res.setdefault(f'sum_colomn_{j+1}', 0) + int(matrix[i][j])
#
# flag = True
#
# for el in res:
#     if sorted(check_list) != numbers:
#         flag = False
#         break
#     if res['main_diagonal'] != res[el]:
#         flag = False
#         break
#
# if flag:
#     print('YES')
# else:
#     print('NO')

# МАГИЧЕСКИЙ КВАДРАТ(ОТ ПРЕПОДАВАТЕЛЯ)
# def is_magic_square(n, matrix):
#     # создаем список для всех чисел правильной матрицы
#     correct_nums = list(range(1, n ** 2 + 1))
#
#     # создаем список для всех чисел нашей матрицы
#     our_nums = []
#     for row in matrix:
#         our_nums.extend(row)
#
#     # если эти списки не равны, значит наша матрица уже не состоит из всех чисел от 1 до n ** 2
#     # значит, мы сразу можем вернуть "NO" и не продолжать дальнейшие проверки
#     our_nums.sort()
#     if our_nums != correct_nums:
#         return "NO"
#
#     # в самой матрице мы уже храним все ряды (строки)
#     rows = matrix.copy()
#
#     # создаем список для всех столбцов
#     columns = []
#     for j in range(n):
#         cur_column = []
#         for i in range(n):
#             cur_column.append(matrix[i][j])
#
#         columns.append(cur_column)
#
#     # создаем список для диагоналей (с двумя пустыми подсписками)
#     diagonals = [[], []]
#     for i in range(n):
#         diagonals[0].append(matrix[i][i])
#         diagonals[1].append(matrix[i][n - 1 - i])
#
#     # соединям все строки, столбцы и диагонали в один список
#     all_lines = rows + columns + diagonals
#
#     # инициализируем переменные для максимальной и минимальной суммы среди всех "линий"
#     # за начальные значения возьмём сумму первой "линии"
#     max_sum = sum(all_lines[0])
#     min_sum = sum(all_lines[0])
#     for line in all_lines:
#         max_sum = max(max_sum, sum(line))
#         min_sum = min(min_sum, sum(line))
#
#     # теперь просто сравниваем максимальную и минимальную суммы
#     # они должны быть равны, т.к. все суммы должны быть равны
#     if max_sum != min_sum:
#         return "NO"
#
#     return "YES"
#
#
# n = int(input())
# matrix = [[int(el) for el in input().split()] for _ in range(n)]
#
# print(is_magic_square(n, matrix))






