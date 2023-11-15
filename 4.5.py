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
def create_matrix(n):
    matrix = [[int(num) for num in input().split()] for _ in range(n)]
    return matrix

n, m = int(input()), int(input())
my_matrix = create_matrix(n)

largest = my_matrix[0][0]
for i in range(n):
    for j in range(m):
        if





