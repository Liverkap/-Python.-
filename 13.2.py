#           *****************       модуль fractions        **********
import math
# В этом уроке мы изучим числовой тип данных Fraction, который представляет из себя обыкновенную дробь, с заданными числителем и знаменателем

#       ************************    Рациональное число  **********



# Создание Fraction

# Создать Fraction число можно несколькими способами:
#
# из целых чисел, передав значения числителя и знаменателя дроби,
# из строки на основании десятичного представления;
# из строки на основании обыкновенной дроби;
# из числа с плавающей точкой (не рекомендуется).

# from fractions import Fraction
#
# num1 = Fraction(3, 4)     # 3 - числитель, 4 - знаменатель
# num2 = Fraction('0.55')
# num3 = Fraction('1/9')
#
# print(num1, num2, num3, sep='\n')


# Нужно быть очень внимательным при создании Fraction чисел из чисел с плавающей точкой (float), потому что float числа
# округляются внутри до ближайшего возможного, а Fraction об этом ничего не знает, поэтому копирует содержимое float

# from fractions import Fraction
#
# num = Fraction(0.34)
#
# print(num)

# !!!!!Не рекомендуется создавать Fraction числа из float чисел. В Fraction попадет уже неправильно округленное число. Создавать Fraction числа нужно из целых чисел, либо из строк!

# При создании рационального числа Fraction, автоматически происходит сокращение числителя и знаменателя дроби.


# from fractions import Fraction
#
# num1 = Fraction(5, 10)
# num2 = Fraction('75/100')
# num3 = Fraction('0.25')
#
# print(num1, num2, num3, sep='\n')

# Так же стоит обратить внимание на вывод дробей, являющихся целыми числами.

# from fractions import Fraction
#
# num1 = Fraction(5, 1)        # 5/1 = 5
# num2 = Fraction(23, 23)      # 23/23 = 1
#
# print(num1, num2, sep='\n')


#       *****************       Сравнение Fraction чисел        ********

# >: больше;
# <: меньше;
# >=: больше либо равно;
# <=: меньше либо равно;
# ==:  в точности равно;
# !=: не равно.

# from fractions import Fraction
#
# num1 = Fraction(1, 2)        # 1/2
# num2 = Fraction(15, 30)      # 15/30=1/2
# num3 = Fraction(3, 5)        # 3/5
# num4 = Fraction(5, 3)        # 5/3
# num5 = 1
# num6 = 0.8
#
#
# print(num1 == num2)
# print(num1 != num4)
# print(num2 > num3)
# print(num4 <= num1)
# print(num1 < num5)
# print(num6 > num4)

# Обратите внимание на то, что мы можем сравнивать Fraction числа и целые числа (числа с плавающей точкой) без явного приведения типов.



#       ********************        Арифметические операции над Fraction числами        *******

# Тип данных Fraction отлично интегрирован в язык Python. С Fraction числами работают все привычные операции: сложение, вычитание, умножение, деление, возведение в степень

# from fractions import Fraction
#
# num1 = Fraction('1/10')
# num2 = Fraction('2/3')
#
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)


# Мы также можем совершать арифметические операции над Fraction и целыми числами (миксовать Fraction и int), но не рекомендуется смешивать их с float.

# from fractions import Fraction
#
# num = Fraction('3/8')
#
# print(num + 1)
# print(num - 1)
# print(num * 2)
# print(num ** 4)

# Обратите внимание, на то, что операция возведения в степень (**) для Fraction чисел может возвращать вещественный результат.

# from fractions import Fraction
#
# num1 = Fraction('3/8')
# num2 = Fraction('1/2')
#
# print(num1 ** num2)

# ***************       Математические функции      ***************

# Fraction числа можно передавать как аргументы функций, ожидающих float. Тогда они будут преобразованы во float. К примеру, модуль math оперирующий float числами, может работать и с Fraction числами.
# from fractions import Fraction
# from math import *
#
# num1 = Fraction('1.44')
# num2 = Fraction('0.523')
#
# print(sqrt(num1))
# print(sin(num2))
# print(log(num1 + num2))

# *****************     Свойства numerator и denominator        *********************
# Для получения числителя и знаменателя Fraction числа используются свойства numerator и denominator

# from fractions import Fraction
#
# num = Fraction('5/16')
#
# print('Числитель дроби равен:', num.numerator)
# print('Знаменатель дроби равен:', num.denominator)

# В Python 3.8 появился метод as_integer_ratio(), который возвращает кортеж, состоящий из числителя и знаменателя данного Fraction числа.

# from fractions import Fraction
#
# num = Fraction('-5/16')
#
# print(num.as_integer_ratio())

# ***************       Метод limit_denominator()       ********

# Метод limit_denominator() возвращает самую близкую к данному числу рациональную дробь, чей знаменатель не превосходит переданного аргумента.
# from fractions import Fraction
# import math
#
# print('PI =', math.pi)
#
# num = Fraction(str(math.pi))
#
# print('No limit =', num)
#
# for d in [1, 5,  50, 90, 100, 500, 1000000]:
#     limited = num.limit_denominator(d)
#     print(limited)

# Метод limit_denominator() позволяет получить очень точные рациональные приближения иррациональных чисел, что очень удобно во многих математических задачах.

# Примечание 1. Для того, чтобы каждый раз не писать название типа, можно использовать следующий код:
# from fractions import Fraction as F
#
# num1 = F('1/5') + F('3/2')
# num2 = F('1/4') * F('2/5')
#
# print(num1)
# print(num2)
#
# Примечание 3.
# В Python нельзя совершать арифметические операции (+, -, *, /) между типами Decimal и Fraction.

# *********************
# from fractions import Fraction
#
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14',
#            '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02',
#            '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31',
#            '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
#
# for el in numbers:
#     print(f'{el} = {Fraction(el)}')


# ***********************

# from fractions import Fraction
#
# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
#
# numbers = [Fraction(el) for el in s.split()]
#
# print(max(numbers) + min(numbers))

# СОКРАТИТЕ ДРОБЬ

# from fractions import Fraction
#
# print(Fraction(int(input()), int(input())))

# ОПЕРАЦИИ НАД ДРОБЯМИ
# from fractions import Fraction as F
#
# a, b = input(), input()
#
# print(f'{a} + {b} = {F(a) + F(b)}')
# print(f'{a} - {b} = {F(a) - F(b)}')
# print(f'{a} * {b} = {F(a) * F(b)}')
# print(f'{a} / {b} = {F(a) / F(b)}')


# ОПЕРАЦИИ НАД ДРОБЯМИ (ОТ ПОЛЬЗОВАТЕЛЯ)
# from fractions import Fraction as F
# operators = {'+': F.__add__, '-': F.__sub__, '*': F.__mul__, '/': F.__truediv__}
# a, b = [input() for _ in '..']
# ops = [*map(F, (a, b))]
# for op in operators:
#     print(f'{a} {op} {b} = {operators[op](*ops)}')

# СУММА ДРОБЕЙ 1
# from fractions import Fraction as F
#
# n = int(input())
# sum = 0
#
# for i in range(1, n + 1):
#     sum += (F(1, i ** 2))
#
# print(F(sum))


# СУММА ДРОБЕЙ 1 (ОТ ПОЛЬЗОВАТЕЛЯ)
# from fractions import Fraction as F
#
# print(sum([F(1, i**2) for i in range(1, int(input()) + 1)]))


# СУММА ДРОБЕЙ 2
# from fractions import Fraction as F
# from math import factorial
#
# numbers = [F(1, factorial(i)) for i in range(1, int(input()) + 1)]
#
# print(sum(numbers))

# СУММА ДРОБЕЙ 2 (ОТ ПОЛЬЗОВАТЕЛЯ)(ЧЕРЕЗ ЗАЦИКЛЕННУЮ ФУНКЦИЮ)
# from fractions import Fraction
# a = int(input())
# s = 0
# def factorial(a: int):
#     if a == 1:
#         return 1
#     return a * factorial(a-1)
# for i in range(1, a+1):
#     s += Fraction(1, factorial(i))
# print(s)

# СУММА ДРОБЕЙ 2 (ОТ ПОЛЬЗОВАТЕЛЯ)(БЕЗ ИСПОЛЬЗОВАНИЯ ФАКТОРИАЛА)
# from fractions import Fraction
#
# n = int(input())
#
# factor = 1
# s = 0
# for i in range(1, n + 1):
#     factor *= i
#     s += Fraction(1, factor)
#
# print(s)

# ЮНЫЙ МАТЕМАТИК
from fractions import Fraction as F
from math import gcd

n = int(input())

numbers = [i for i in range(1, n)]
print(numbers)

print(math.gcd(3, 5))




