#                   ******  модуль decimal**

# В прошлых уроках мы изучили два числовых типа данных, представленных в Python:
#
# int – целое число;
# float – число с плавающей точкой (аналог вещественного числа в математике).

# В Python есть три дополнительных числовых типа данных:
#
# Decimal – десятичное число, для выполнения точных расчетов;
# Fraction – число, представляющее собой обыкновенную дробь, с заданным числителем и знаменателем;
# Complex – комплексное число.


#   *********************   Тип данных float    *****

# if 0.3 == 0.3:
#     print('YES')
# else:
#     print('NO')

# *************
# num = 0.1 + 0.1 + 0.1
#
# if num == 0.3:
#     print('YES')
# else:
#     print('NO')


# чтобы сравнивать два float числа мы должны использовать такой код:
# num = 0.1 + 0.1 + 0.1
# eps = 0.000000001           # точность сравнения
#
# if abs(num - 0.3) < eps:    # число num отличается от числа 0.3 менее чем 0.000000001
#     print('YES')
# else:
#     print('NO')

# Не стоит сравнивать float числа с помощью оператора ==. Для сравнения float чисел нужно использовать указанный выше код.


# **************        Тип данных Decimal  ***********

# Тип данных Decimal – это класс из стандартного модуля decimal. Он представляет собой число с плавающей точкой, как и float. Однако, Decimal имеет ряд существенных отличий от float.
# Тип Decimal создан, чтобы операции над вещественными числами в компьютере выполнялись как в математике, и равенство 0.1+0.1+0.1==0.3 было верным.
# Точность результатов арифметических действий очень важна для научных вычислений, в сфере финансов и бизнеса. Для таких задач тип данных float не подходит.

# В Python тип данных float реализован по стандарту IEEE-754 как число с плавающей точкой двойной точности (64 бита) с основанием экспоненты равным 2.
# Реализация таких чисел заложена прямо в железо любого современного процессора. Поэтому float в Python работает
# как аналогичный тип данных double в таких языках программирования как С#, С++, Java и т.д. И имеет такие же ограничения
# # и «странности». Так как float поддерживается аппаратно, быстродействие при использовании этого типа данных сравнительно велико.

# Тип данных Decimal реализован программно, поэтому он в разы медленнее типа данных float, реализованного аппаратно. Сам тип данных Decimal написан на языке С.
# Тип данных Decimal оперирует числами с произвольной – задаваемой программистом, но конечной точностью. По умолчанию точность составляет 28 десятичных знаков.

# Тип данных Decimal неизменяемый. Операции над ним приводят к созданию новых объектов, при этом старые не меняются.

# Еще одно следствие того, что Decimal реализован программно – его можно на ходу настраивать, как угодно программисту.
# Для этого есть контекст – объект, содержащий настройки для выполнения операций. Операции, выполняемые в контексте,
# следуют заданным в нем правилам. Для float все правила фиксированы на аппаратном уровне.

# Для типа данных Decimal можно настроить:
#
# точность выполнения операций в количестве десятичных знаков;
# режимы округления;
# режимы обработки исключительных ситуаций (деление на ноль, переполнение и т. д).


#   ****************    Создание Decimal чисел  ***********

# Создать Decimal число можно из обычного целого числа (int), из числа с плавающей точкой (float) или из строки (str)

# from decimal import *
#
# d1 = Decimal(1)
# d2 = Decimal(567)
# d3 = Decimal(-93)
# d4 = Decimal('12345')
# d5 = Decimal('52.198')
#
# print(d1, d2, d3, d4, d5, sep='\n')

# При создании Decimal чисел из чисел с плавающей точкой (float) возникают проблемы, так как float числа округляются внутри до ближайшего возможного, а Decimal об этом ничего не знает и копирует содержимое float
# from decimal import *
#
# num = Decimal(0.1)
#
# print(num)

#       *************   Арифметические операции над Decimal числами **********

# Тип данных Decimal отлично интегрирован в язык Python. С Decimal числами работают все привычные операции: сложение, вычитание, умножение, деление, возведение в степень.

# from decimal import *
#
# num1 = Decimal('5.2')
# num2 = Decimal('2.3')
#
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 // num2)
# print(num1 ** num2)
#
# Можно совершать арифметические операции над Decimal и целыми числами (миксовать Decimal и int), но не рекомендуется смешивать их с float

# from decimal import *
#
# num = Decimal('5.2')
#
# print(num + 1)
# print(num - 10)
# print(num * 2)
# print(num ** 4)

# ****************      Математические функции      ********

# Decimal числа можно передавать как аргументы функциям, ожидающим float. Они будут преобразованы во float. К примеру, модуль math, оперирующий float числами, может работать и с Decimal числами.
# from decimal import *
# from math import *
#
# num1 = Decimal('1.44')
# num2 = Decimal('0.523')
#
# print(sqrt(num1))
# print(sin(num2))
# print(log(num1 + num2))

# **********
# from decimal import *
#
# num = Decimal('10.0')
#
# print(num.sqrt())
# print(num.exp())
# print(num.ln())
# print(num.log10())

# **********
# Тип данных Decimal также содержит полезный метод as_tuple() который возвращает кортеж из 3 элементов:
#
# sign – знак числа ( 0 для положительного числа и 1 для отрицательного числа);
# digits – цифры числа;
# exponent – значение экспоненты (количество цифр после точки, умноженное на −1),

# from decimal import *
#
# num1 = Decimal('-1.4568769017')
# num2 = Decimal('0.523')
#
# print(num1.as_tuple())
# print(num2.as_tuple())


# from decimal import *
#
# num = Decimal('-1.4568769017')
# num_tuple = num.as_tuple()
#
# print(num_tuple.sign)
# print(num_tuple.digits)
# print(num_tuple.exponent)

# ***********   Работа с контекстом Decimal чисел   *************
# Базовые параметры Decimal можно посмотреть в его контексте, выполнив функцию getcontext().

# from decimal import *
#
# print(getcontext())

#                   **********  Точность чисел  *************
# Контекстом в Decimal можно управлять, устанавливая свои значения. Например, чтобы управлять точностью Decimal,
# необходимо изменить параметр контекста prec (от англ. precision – точность). При этом точность вступает в силу только во время арифметических операций, а не при создании самих чисел.

# from decimal import *
#
# getcontext().prec = 3      # устанавливаем точность в 3 знака
#
# num = Decimal('3.1415')
#
# print(num)
# print(num * 1)
# print(num * 2)
# print(num / 2)


# ******************    Округление чисел   *********
# Округляют числа Decimal с помощью метода quantize(). Этот метод в качестве первого аргумента принимает объект Decimal, указывающий на формат округления.

# from decimal import *
#
# getcontext().prec = 4                    # устанавливаем точность числа
#
# num = Decimal('3.1415926535')
#
# print(num.quantize(Decimal('1.000')))    #  округление до 3 цифр в дробной части
# print(num.quantize(Decimal('1.00')))     #  округление до 2 цифр в дробной части
# print(num.quantize(Decimal('1.0')))

# Если точность округления установлена в 2 , а формат округления Decimal('1.00'), то возникнет ошибка.


# Помимо первого параметра, метод quantize() принимает в качестве второго параметра стратегию округления:
#
# ROUND_CEILING – округление в направлении бесконечности (Infinity);
# ROUND_FLOOR – округляет в направлении минус бесконечности (- Infinity);
# ROUND_DOWN – округление в направлении нуля;
# ROUND_HALF_EVEN – округление до ближайшего четного числа, число 6.5 округлится не до 7, а до 6;
# ROUND_HALF_DOWN – округление до ближайшего нуля;
# ROUND_UP – округление от нуля;
# ROUND_05UP – округление от нуля (если последняя цифра после округления до нуля была бы 0 или 5, в противном случае к нулю).


# from decimal import *
#
# num = Decimal('3.456')
#
# print(num.quantize(Decimal('1.00'), ROUND_CEILING))
# print(num.quantize(Decimal('1.00'), ROUND_FLOOR))



#               ***********         Сравнение float и Decimal чисел     ****
# Выбор между типами данных Decimal и float – поиск компромисса в условиях конкретной задачи.
#
# Если нужно считать очень много (симуляции, физика, графика, игры), имеет смысл отказаться от точности Decimal в пользу
# скорости и компактности хранения данных float. В бизнесе и финансах считать приходится не так много, но делать это
# нужно предельно точно, тут имеет смысл посмотреть в сторону Decimal

# **************
# Примечание 1. Decimal числа можно сравнивать между собой, как обычные числа, причем в отличие от float чисел допускается и точное равенство.

# from decimal import *
#
# num = Decimal('0.1')
# if num*3 == Decimal('0.3'):
#     print('YES')
# else:
#     print('NO')


# Примечание 2. Можно сортировать списки с Decimal числами и искать минимум и максимум среди них.
#
# from decimal import *
#
# s = '1.34 3.45 1.00 0.03 9.25'
#
# numbers = [Decimal(i) for i in s.split()]
#
# maximum = max(numbers)
# minimum = min(numbers)
#
# numbers.sort()
#
# print(maximum)
# print(minimum)
# print(numbers)


# ****************
# from decimal import Decimal as D
#
# num1 = D('1.5') + D('3.2')
# num2 = D('1.4') * D('2.58')
#
# print(num1)
# print(num2)


# from decimal import *
#
# num = Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3)
#
# if num == 0:
#     print('YES')
# else:
#     print('NO')


# *********
# from decimal import *
#
# s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
#
# my_list = s.split()
# sum = Decimal(min(my_list)) + Decimal(max(my_list))
# print(sum)


# ********
# from decimal import *
#
# s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
#
# numbers = [Decimal(num) for num in s.split()]
# numbers.sort(reverse=True)
# sum = 0
#
# for el in numbers:
#     sum += el
#
# print(sum)
# print(*numbers[:5])

# ********* (ОТ ПОЛЬЗОВАТЕЛЯ)

# from decimal import Decimal as D
#
# s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
#
# nums = [D(x) for x in s.split()]
#
# print(sum(nums))
# print(*sorted(nums, reverse=True)[:5])






