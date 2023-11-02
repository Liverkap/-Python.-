#               ****************  ТИП ДАННЫЕХ BOOL      ***************
#
# numbers = [1, 2, 3, 4, 5, 8, 10, 12, 15, 17]
# res = 0
#
# for num in numbers:
#     res += (num % 2 == 0)
#
# print(res)


# Примечание 1. Вместо избыточного кода:

# if flag == True:
#
# # программисты обычно пишут код:
# if flag:


# Аналогично вместо кода
# if flag == False:
# пишут
# if not flag:


# num1 = 3 * True - (True - False)
# num2 = (True + True + False) ** 3 + 5
# print(num1 + num2)


# numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
# res = 0
# for num in numbers:
#     res += (num % 2 == 1) and (num > 1)
# print(res)


# ФУНКЦИЯ BOOL()

# строки: пустая строка — ложь (False), непустая строка — истина (True);
# числа: нулевое число — ложь (False), ненулевое число (в том числе и меньшее нуля) — истина (True);
# списки: пустой список — ложь (False), непустой — истина (True).

# print(bool('Beegeek'))
# print(bool(17))
# print(bool(['apple', 'cherry']))
# print(bool())
# print(bool(''))
# print(bool(0))
# print(bool([]))


# ФУНКЦИИ, ВОЗВРАЩАЮЩИЕ БУЛЕВО ЗНАЧЕНИЕ
# Мы можем создавать функции, возвращающие булевы значения (True или False). Такая практика очень полезна.
# Напишем функцию is_even(), принимающую одно число и возвращающую значение True, если переданное число четное и False - в противном случае:
# def is_even(num):
#     return num % 2 == 0
#
# print(is_even(8))
# print(is_even(7))

# В программировании функция, которая возвращает значение True или False, называется предикатом.!!!!!!


# ФУНКЦИЯ ISINSTANCE() - встроенная функция isinstance() для проверки соответствия типа объекта какому-либо типу данных.
#
# print(isinstance(3, int))
# print(isinstance(3.5, float))
# print(isinstance('Beegeek', str))
# print(isinstance([1, 2, 3], list))
# print(isinstance(True, bool))


# ФУНКЦИЯ TYPE() - встроенная функция type(), позволяющая получить тип указанного в качестве аргумента объекта!!!

# print(type(3))
# print(type(3.5))
# print(type('Beegeek'))
# print(type([1, 2, 3]))
# print(type(True))


# Обратите внимание, что при проверке типов обычно вместо функции type() используется функция isinstance(),
# так как она принимает во внимание иерархию типов (ООП).

# print(bool(0.0))


# ПРЕДИКАТ ДЕЛИМОСТИ

# def is_even(num1, num2):
#     return num1 % num2 == 0
#
# a, b = int(input()), int(input())
#
# if is_even(a, b):
#     print('делится')
# else:
#     print('не делится')

