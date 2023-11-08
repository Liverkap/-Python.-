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
n = 4                                         # количество строк (элементов)
my_list = []

for _ in range(n):
    elem = [int(i) for i in input().split()]  # создаем список из элементов строки
    my_list.append(elem)

print(my_list)


