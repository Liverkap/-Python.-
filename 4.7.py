#                                   СЛОЖЕНИЕ МАТРИЦ

# Складывать можно только матрицы одинаковой размерности с равным количеством строк и столбцов


#                                      Свойства сложения матриц

# 1. Коммутативность – результат сложения матриц не зависит от их перестановки
# A+B=B+A;

# 2. Ассоциативность – результат сложения матриц не зависит от расстановки скобок
# A+(B+C)=(A+B)+C

# 3. Сложение с нулевой матрицей – для любой матрицы существует нейтральный элемент, которым является нулевая матрица,
# сложение с которым не изменяет исходную матрицу. Нулевая матрица – матрица, все элементы которой имеют нулевое значение
# A+0=0+A=A

# 4. Существование противоположной матрицы – для ненулевой матрицы A всегда есть матрица −A, сложение с которой даст в результате нулевую матрицу:
# A+(−A)=0


#                                        Умножение матрицы на число

# Операция умножения матрицы на число k заключается в построении матрицы и kA=[k⋅aij].
# Умножать на число можно матрицы любого размера. В результате умножения получается матрица того же размера, что исходная.

# Произведение матрицы A на число k – результирующая матрица B=kA того же размера,
# полученная умножением каждого из элементов aij исходной матрицы на заданное число


#                                    Свойства умножения матрицы на число

# 1. Единица – нейтральное число умножения любой матрицы, результат умножения на нейтральное число – исходная матрица:
# 1×A=A
#
# 2. Результат умножения любой матрицы на ноль – нулевая матрица, все элементы которой равны нулю
# 0×A=0
#
# 3. Для матриц одного размера и действительного числа выполняется свойство дистрибутивности умножения относительно сложения:
# k×(A+B)=k×A+k×B
#
# 4. Для любой матрицы и суммы действительных чисел выполняется свойство дистрибутивности
# (k+n)×A=k×A+n×A
#
# 5. Для любой матрицы и произведения любых действительных чисел выполняется свойство ассоциативности умножения
# (k×n)×A=k×(n×A)


#                                       Умножение матрицы на матрицу

# Умножение двух матриц A и  B – вычисление результирующей матрицы  C, каждый элемент cij которой равен сумме
# произведений элементов соответствующих строки первой матрицы air и столбца второй матрицы brj

# Одну матрицу можно умножать на другую только тогда, когда количество столбцов в первой матрице совпадает с количеством
# строк во второй матрице. То есть матрицы должны быть согласованы по размерности


#                                         Свойства умножения матриц

# 1. Ассоциативность – (A× B)× C =A×(B× C)
# 2. Дистрибутивность – A×(B+C)=A×B+A×C,(A+B)×C=A×C+B×C
# 3. Ассоциативность и коммутативность относительно умножения на число – (k×A)×B=k×(A×B)=A×(k×B)
# 4. В общем случае умножение матриц не коммутативно – A×B!=B×A


# перемножение матриц
# n1 = 3 # размерность первой матрицы
# m1 = 3
# n2 = 3 # размерность второй матрицы
# m2 = 3
#
# matrix1 = [[1,1,1], [2,2,2], [3,3,3]]
# matrix2 = [[1,2,3], [4,5,6], [7,8,9]]
#
# # можно добавить условие, если m1 != n2 - вывести ошибку что размерности не совпадают
# # тогда уже не имеет смысла переходить к циклу
#
# #  размерность итоговой матрицы должна быть n1хm2
# result = [[0] * m2 for _ in range(n1)]
#
#
# # внешний цикл - по элементам итоговой матрицы
# for i in range(n1):
#     for j in range(m2):
#        # за один проход третьего цикла строка первой матрицы умножается на столбец второй
#        # затем переход к следующей строке и стобцу и тд
#        # поэтому размерность цикла - m1 - это количество строк первой и столбцов второй
#         for k in range(m1):
#             result[i][j] += matrix1[i][k] * matrix2[k][j]
#
# for row in result:
#     for column in row:
#         print(str(column).ljust(3), end=" ")
#     print()
#
#
# перемножение матриц с помощью НАМПАЙ
# import numpy as np
#
# matrix1 = np.array([[1,1,1], [2,2,2], [3,3,3]])
# matrix2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
#
# result = matrix1.dot(matrix2)
#
# for row in result:
#     for column in row:
#         print(str(column).ljust(3), end=" ")
#     print()



# matrix = [[1, 0], [4, 1]]
# new_matrix = [[None] * len(matrix[0]) for _ in range(len(matrix[1]))]
#
# for q in range(25):
#     for i in range(len(matrix[0])):
#         for j in range(len(matrix[1])):
#             new_matrix[i][j] = matrix[i][j] * matrix[j][i]
#
#
# print(new_matrix)


# СЛОЖЕНИЕ МАТРИЦ

# n, m = [int(num) for num in input().split()]
#
# mtrx_1 = [[int(num) for num in input().split()] for _ in range(n)]
# input()
# mtrx_2 = [[int(num) for num in input().split()] for _ in range(n)]
# res_mtrx = [[None] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         res_mtrx[i][j] = mtrx_1[i][j] + mtrx_2[i][j]
#
# for row in res_mtrx:
#     print(*row)


# УМНОЖЕНИЕ МАТРИЦ

# n, m = [int(num) for num in input().split()]
#
# matrix_A = [[int(num) for num in input().split()] for _ in range(n)]
# input()
#
# m, k = [int(num) for num in input().split()]
# matrix_B = [[int(num) for num in input().split()] for _ in range(m)]
# matrix_C = [[0] * k for _ in range(n)]
#
#
# for i in range(n):
#     for j in range(k):
#         for r in range(m):
#             matrix_C[i][j] += matrix_A[i][r] * matrix_B[r][j]
#
# for row in matrix_C:
#     print(*row)


# ВОЗВЕДЕНИЕ МАТРИЦЫ В СТЕПЕНЬ
# import copy
# n = int(input())
#
# matrix = [[int(num) for num in input().split()] for _ in range(n)]
# m = int(input())
# res_matrix = [[0] * n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         for r in range(n):
#             res_matrix[i][j] += matrix[i][r] * matrix[r][j]
#
#
# while m != 2:
#     cur_matrix = copy.deepcopy(res_matrix)
#     new_mat = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             for r in range(n):
#                 new_mat[i][j] += cur_matrix[i][r] * matrix[r][j]
#
#     res_matrix = copy.deepcopy(new_mat)
#     m -= 1
#
#
# for row in res_matrix:
#     print(*row)


# ВОЗВЕДЕНИЕ МАТРИЦЫ В СТЕПЕНЬ(ОТ ПРЕПОДАВАТЕЛЯ)
# def square_matrix_mult(matrixA, matrixB, size):
#     matrixC = [[0] * size for _ in range(size)]
#     for i in range(size):
#         for j in range(size):
#             for q in range(size):
#                 matrixC[i][j] += matrixA[i][q] * matrixB[q][j]
#     return matrixC
#
#
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# m = int(input())
# powered_matrix = matrix.copy()
#
# for _ in range(m - 1):
#     powered_matrix = square_matrix_mult(matrix, powered_matrix, n)
#
# for row in powered_matrix:
#     print(*row)

# ВОЗВЕДЕНИЕ МАТРИЦЫ В СТЕПЕНЬ(ОТ ПОЛЬЗОВАТЕЛЯ)
# n = int(input())
# matrix_1 = [[int(i) for i in input().split()] for _ in range(n)]
# m = int(input())
# matrix_2 = matrix_1
# matrix = [[0] * n for _ in range(n)]
#
# for _ in range(m - 1):
#     for i in range(n):
#         for j in range(n):
#             for x in range(n):
#                 matrix[i][j] += matrix_1[i][x] * matrix_2[x][j]
#     matrix_1 = matrix
#     matrix = [[0] * n for _ in range(n)]
#
# for row in matrix_1:
#     print(*row)

# ВОЗВЕДЕНИЕ МАТРИЦЫ В СТЕПЕНЬ(ОТ ПОЛЬЗОВАТЕЛЯ)
# def matrix_mult(m1, m2, n):
#     return [[sum(m1[i][k] * m2[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
#
#
# n = int(input())
# a = [[*map(int, input().split())] for _ in range(n)]
# # в качестве начального значения создаём единичную матрицу E
# # у которой на главной диагонали все единицы. Она играет роль
# # единицы при умножении матриц, т.е. E * A = A
# res = [[0] * n for _ in range(n)]
# for i in range(n):
#     res[i][i] = 1
#
# m = int(input())
# while m:
#     if m % 2 != 0:
#         res = matrix_mult(res, a, n)  # умножение на матрицу a
#     a = matrix_mult(a, a, n)  # возведение в квадрат
#     m //= 2
#
# for row in res:
#     print(*row)
