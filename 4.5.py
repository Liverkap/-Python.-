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

n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]

for el in matrix:
    print(*el)


# ХОДЫ КОНЯ




