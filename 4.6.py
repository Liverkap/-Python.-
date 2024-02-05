# ШАХМАТНАЯ ДОСКА

# n, m = [int(num) for num in  input().split()]
#
# matrix = [['.'] * m for _ in range(n)]
#
#
# for i in range(0, n, 2):
#     for j in range(1, m, 2):
#         matrix[i][j] = '*'
#
# for i in range(1, n, 2):
#     for j in range(0, m, 2):
#         matrix[i][j] = '*'
#
# for row in matrix:
#     print(*row)
#
# # ШАХМАТНАЯ ДОСКА(ОТ ПРЕПОДАВАТЕЛЯ)
# n, m = [int(i) for i in input().split()]
# board = [['.'] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(1 - i % 2, m, 2):
#         board[i][j] = '*'
#
# for row in board:
#     print(*row)

# # ШАХМАТНАЯ ДОСКА(ОТ ПОЛЬЗОВАТЕЛЯ)
# n, m = map(int, input().split())
# b = [['.*'[(i + j) % 2] for j in range(m)] for i in range(n)]
# for row in b:
#     print(*row)


# ПОБОЧНАЯ ДИАГОНАЛЬ

# n = int(input())
# matrix = [[0] * n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         matrix[i][n - i - 1] = 1
#         if (i > j and i > n - j - 1) or (i <= j and i > n - j - 1):
#             matrix[i][j] = 2
#
#
# for row in matrix:
#     print(*row)
#
#
# # ПОБОЧНАЯ ДИАГОНАЛЬ (ОТ ПРЕПОДАВАТЕЛЯ)
# n = int(input())
# matrix = [[None for _ in range(n)] for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i + j + 1 == n:
#             matrix[i][j] = 1
#         elif i + j + 1 < n:
#             matrix[i][j] = 0
#         else:
#             matrix[i][j] = 2
#
# for row in matrix:
#     print(*row)
#
# # ПОБОЧНАЯ ДИАГОНАЛЬ (ОТ ПОЛЬЗОВАТЕЛЯ)
# n = int(input())
# board = [[0] * (n - i - 1) + [1] + [2] * i for i in range(n)]
#
# for row in board:
#     print(*row)


# ЗАПОЛНЕНИЕ 1

# n, m = [int(num) for num in input().split()]
#
# matrix = [[None] * m for _ in range(n)]
#
# count = 1
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = str(count).ljust(3)
#         count += 1
#
# for row in matrix:
#     print(*row)


# ЗАПОЛНЕНИЕ 1 (БЕЗ СОЗДАНИЯ МАТРИЦЫ)
# n, m = [int(num) for num in input().split()]
#
# count = 1
# for i in range(n):
#     for j in range(m):
#         print(str(count).ljust(3), end=' ')
#         count += 1
#     print()

# print(matrix)

# ЗАПОЛНЕНИЕ 1(ОТ ПРЕПОДАВАТЕЛЯ)
# n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = i * m + j + 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()
#
# # ЗАПОЛНЕНИЕ 1(ОТ ПРЕПОДАВАТЕЛЯ)
# n, m = [int(i) for i in input().split()]
# matrix = [list(range(m*i + 1, m*i + 1 + m)) for i in range(n)]

# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()

# ЗАПОЛНЕНИЕ 1(ОТ ПОЛЬЗОВАТЕЛЯ)
# n, m = [int(i) for i in input().split()]
#
# for i in range(1, (n * m) + 1):
#     print(str(i).ljust(2), end=' ')
#     if i % m == 0:
#         print()

# ЗАПОЛНЕНИЕ 1(ОТ ПОЛЬЗОВАТЕЛЯ)
# n, m = map(int, input().split())
#
# count = 1
#
# for i in range(n):
#     for j in range(m):
#         print(f'{count:3}', end=' ')
#         count += 1
#     print()


# ЗАПОЛНЕНИЕ 2

# n, m = [int(num) for num in input().split()]
# matrix = [[None] * m for _ in range(n)]
#
# count = 1
# for i in range(m):
#     for j in range(n):
#         matrix[j][i] = str(count).ljust(3)
#         count += 1
#
# for row in matrix:
#     print(*row)

# ЗАПОЛНЕНИЕ 2(ОТ ПРЕПОДАВАТЕЛЯ)
# n, m = [int(i) for i in input().split()]
# matrix = [
#     list(range(i + 1, i + 1 + n * (m - 1) + 1, n))
#     for i in range(n)
# ]
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=" ")
#     print()
#
# # ЗАПОЛНЕНИЕ 2(ОТ ПОЛЬЗОВАТЕЛЯ)
# n, m = [int(x) for x in input().split()]
#
# res = [[str(i + j * n + 1).ljust(2) for j in range(m)] for i in range(n)]
#
# for x in res:
#     print(*x)


# ЗАПОЛНЕНИЕ 3

# n = int(input())
# matrix = [[str(0).ljust(3)] * n for _ in range(n)]
#
# for i in range(n):
#     matrix[i][i] = str(1).ljust(3)
#     matrix[n-i-1][i] = str(1).ljust(3)
#
# for row in matrix:
#     print(*row)
#
# # ЗАПОЛНЕНИЕ 3(ОТ ПРЕПОДАВАТЕЛЯ)
# n = int(input())
# matrix = [[0 for _ in range(n)] for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i == j or i + j + 1 == n:
#             matrix[i][j] = 1
#
# for row in matrix:
#     print(*row)
#
# # ЗАПОЛНЕНИЕ 3(ОТ ПОЛЬЗОВАТЕЛЯ)
# n = int(input())
# matr = [[0] * n for _ in range(n)]
# for i in range(n):
#     matr[i][i] = 1
#     matr[i][n - 1 - i] = 1
# for i in range(n):
#     for j in range(n):
#         print(str(matr[i][j]).ljust(3), end='')
#     print()

# ЗАПОЛНЕНИЕ 4

# n = int(input())
#
# matrix = [[0] * n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if (i <= j and i <= n - j - 1) or (i >= j and i >= n - j - 1):
#             matrix[i][j] = 1
#
# for row in matrix:
#     print(*row)

# ЗАПОЛНЕНИЕ 4(ОТ ПРЕПОДАВАТЕЛЯ)
# n = int(input())
# matrix = [[0] * n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if (i <= j and i + j + 1 <= n) or (i >= j and i + j + 1 >= n):
#             matrix[i][j] = 1
#
# for i in range(n):
#     for j in range(n):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()


# ЗАПОЛНЕНИЕ 5

# n, m = [int(num) for num in input().split()]
#
# matrix = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = (i + j) % m + 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()


# ЗАПОЛНЕНИЕ ЗМЕЙКОЙ

# n, m = [int(num) for num in input().split()]
#
# matrix = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         if i % 2 == 0:
#             matrix[i][j] = i * m + j + 1
#         else:
#             matrix[i][j] = (i + 1) * m - j
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()

# ЗАПОЛНЕНИЕ ЗМЕЙКОЙ(ОТ ПРЕПОДАВАТЕЛЯ)
# n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = i * m + j + 1
#     if i % 2:
#         matrix[i].reverse()
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()

# ЗАПОЛНЕНИЕ ЗМЕЙКОЙ(ОТ ПОЛЬЗОВАТЕЛЯ)
# n, m = map(int, input().split())
# matrix = [range(m*i+1, m*i+1 + m)[::i%2*-2+1] for i in range(n)]
# [print(*row) for row in matrix]





