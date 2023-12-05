#           *********** Объединение множеств: метод union() ***********
#
# Объединение множеств – это множество, состоящее из элементов, принадлежащих хотя бы одному из объединяемых множеств.
# Для этой операции существует метод union().

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset1.union(myset2)
# print(myset3)

# myset3 = myset1 | myset2
# print(myset3)


#       ******************   Пересечение множеств: метод intersection() ***************

# Пересечение множеств – это множество, состоящее из элементов, принадлежащих одновременно каждому из пересекающихся множеств.
# Для этой операции существует метод intersection()

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}

# myset3 = myset1.intersection(myset2)
# print(myset3)

# myset3 = myset1 & myset2
# print(myset3)

# myset1.intersection_update(myset2) #Обновление существующего множества
# print(myset1)


#               *****************   Разность множеств: метод difference()   ***************

# Разность множеств – это множество, в которое входят все элементы первого множества, не входящие во второе множество.
# Для этой операции существует метод difference()

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}

# myset3 = myset1.difference(myset2)
# print(myset3)

# myset3 = myset1 - myset2
# print(myset3)

# myset3 = myset2 - myset1
# print(myset3)


#           **************  Симметрическая разность: метод symmetric_difference()       ***************

# Симметрическая разность множеств – это множество, включающее все элементы исходных множеств, не принадлежащие одновременно
# обоим исходным множествам. Для этой операции существует метод symmetric_difference()

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# # myset3 = myset1.symmetric_difference(myset2)
# # print(myset3)
#
# myset3 = myset1 ^ myset2
# print(myset3)


#           ******************  Методы множеств, изменяющие текущие множества      **************

#           ****************     Метод update() ******
# Метод update() изменяет исходное множество по объединению.
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# #
# # myset1.update(myset2)  # изменяем множество myset1
# # print(myset1)
#
# myset1 |= myset2
# print(myset1)

#           *************       Метод intersection_update() **************

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset1.intersection_update(myset2)  # изменяем множество myset1
# print(myset1)
#
# myset1 &= myset2
# print(myset1)


#           ******************* Метод difference_update()   ***********

# Метод difference_update() изменяет исходное множество по разности.

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset1.difference_update(myset2)  # изменяем множество myset1
# print(myset1)
#
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset1 -= myset2
# print(myset1)


#           ******************* Метод symmetric_difference_update() *********

# Метод symmetric_difference_update() изменяет исходное множество по симметрической разности.
#
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset1.symmetric_difference_update(myset2)  # изменяем множество myset1
# print(myset1)
#
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset1 ^= myset2
# print(myset1)



# Все основные операции над множествами выполняются двумя способами: при помощи метода или соответствующего ему оператора.
# Различие заключается в том, что метод может принимать в качестве аргумента не только множество (тип данных set), но и любой итерируемый объект (список, строку, кортеж..).


# mylist = [2021, 2020, 2019, 2018, 2017, 2016]
# mytuple = (2021, 2020, 2016)
# mystr = 'abcd'
#
# myset = {2009, 2010, 2016}
#
# print(myset.union(mystr))                      # объединяем со строкой
# print(myset.intersection(mylist))              # пересекаем со списком
# print(myset.difference(mytuple))               # находим разность с кортежем


# Некоторые методы (union(), intersection(), difference()) и операторы (|, &, -, ^) позволяют совершать операции над несколькими множествами сразу.

# myset1 = {1, 2, 3, 4, 5, 6}
# myset2 = {2, 3, 4, 5}
# myset3 = {5, 6, 7, 8}
#
# union1 = myset1.union(myset2, myset3)
# union2 = myset1 | myset2 | myset3
#
# difference1 = myset1.difference(myset2, myset3)
# difference2 = myset1 - myset2 - myset3           # порядок выполнения слева-направо
#
# print(union1 == union2)
# print(difference1 == difference2)

# Оператор ^ симметрической разности позволяет использовать несколько множеств, а метод symmetric_difference() – нет.

# myset1 = {1, 2, 3, 4, 5, 6}
# myset2 = {2, 3, 4, 7}
# myset3 = {6, 20, 30}
#
# symdifference = myset1 ^ myset2 ^ myset3  # порядок выполнения слева-направо
#
# print(symdifference)


# КОЛИЧЕСТВО СОВПАДАЮЩИХ

# myset1 = set(input().split())
# myset2 = set(input().split())
#
# union_set = myset1 & myset2
# print(len(union_set))
#
# # КОЛИЧЕСТВО СОВПАДАЮЩИХ (ОТ ПОЛЬЗОВАТЕЛЯ)
# s1 = set(input().split())
# s2 = set(input().split())
# print(len(s1 & s2))
#
#
# # КОЛИЧЕСТВО СОВПАДАЮЩИХ (В 1 СТРОКУ)
#
# print(len(set(input().split()) & set(input().split())))


# ОБЩИЕ ЧИСЛА

# myset1 = set(input().split())
# myset2 = set(input().split())
#
# myset3 = myset1 & myset2
# mylist = []
# for el in myset3:
#     mylist.append(int(el))
#
# print(*sorted(mylist))

# ОБЩИЕ ЧИСЛА (ОТ ПРЕПОДАВАТЕЛЯ)

# set1 = set(int(i) for i in input().split())
# set2 = set(int(i) for i in input().split())
#
# print(*sorted(set1 & set2))


# ЧИСЛА ПЕРВОЙ СТРОКИ

# myset1 = set([int(el) for el in input().split()])
# myset2 = set([int(el) for el in input().split()])
#
# print(*sorted(myset1 - myset2))


# ОБЩИЕ ЦИФРЫ

# n = int(input())
# myset = set(input())
#
# for _ in range(n - 1):
#     myset &= set(input())
#
# print(*sorted(myset))


# ОБЩИЕ ЦИФРЫ (ОТ ПОЛЬЗОВАТЕЛЯ)

# n = int(input())
# numbers = [input() for _ in range(n)]
#
# num_set = set(numbers[0]).intersection(*numbers)
# print(*sorted(num_set))
