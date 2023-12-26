# *****************
# import random
#
# n = 1000
# k = 0
# s0 = 1
# for _ in range(n):
#     x = random.uniform(0, 1)     # случайное число с плавающей точкой от 0 до 1
#     y = random.uniform(0, 1)     # случайное число с плавающей точкой от 0 до 1
#
#     if y <= x**2:                # если попадает в нужную область
#         k += 1
#
# print((k/n)*s0)


# **************
# import random
#
# n = 1000
# k = 0
# s0 = 16
# for _ in range(n):
#     x = random.uniform(-2, 2)
#     y = random.uniform(-2, 2)
#
#     if y**3 - 2*x**2 <= -1 and 2*y + x**3 <= 3:
#         k += 1
#
# print((k/n)*s0)


# *****************
# import random
#
# n = 10 ** 6
# k = 0
# s0 = 16
#
# for _ in range(n):
#     x = random.uniform(-2, 2)
#     y = random.uniform(-2, 2)
#
#     if (x ** 3 + y ** 4 + 2) >= 0 and (3 * x + y ** 2) <= 2:
#         k += 1
#
# print((k/n) * s0)

# *************
# import random
#
# n = 10 ** 6
# k = 0
# s0 = 4
#
# for _ in range(n):
#     x = random.uniform(-1, 1)
#     y = random.uniform(-1, 1)
#
#     if x ** 2 + y ** 2 - 1 <= 0:
#         k += 1
#
# print((k/n) * s0)


# Болотная сортировка

# import random
#
# def is_sort(nums):                   # отсортирован ли список?
#     for i in range(len(nums) - 1):
#         if nums[i] > nums[i + 1]:
#             return False
#     return True
#
# def bogosort(nums):                  # реализация алгоритма болотной сортировки
#     while not is_sort(nums):
#         random.shuffle(nums)
#     return nums
#
# numbers = list(range(10))
# random.shuffle(numbers)              # перемешиваем начальный список
# print(numbers)                       # выводим начальный список
#
# sorted_numbers = bogosort(numbers)
#
# print(sorted_numbers)