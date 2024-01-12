#                           встроенные функции map(), filter(), reduce()

# Язык Python имеет встроенные реализации функций высшего порядка map(), filter() и reduce() , которые намного удобнее, чем наши собственные версии.
#
# Встроенная функция map() имеет сигнатуру map(func, *iterables). В отличие от нашей версии из прошлого урока, встроенная функция map() может принимать сразу несколько последовательностей, переменное количество аргументов.

# def increase(num):
#     return num + 7
#
#
# numbers = [1, 2, 3, 4, 5, 6]
# new_numbers = map(increase, numbers)     #  используем встроенную функцию map()
#
# print(new_numbers)

# Такой объект похож на список тем, что его можно перебирать циклом for, то есть итерировать. Такие объекты в Python называют итераторами!!!


# def increase(num):
#     return num + 7
#
#
# numbers = [1, 2, 3, 4, 5, 6]
# new_numbers = map(increase, numbers)
#
# for num in new_numbers:  # итерируем циклом for
#     print(num)

# Чтобы получить из итератора список, нужно воспользоваться функцией list()

# new_numbers = list(map(increase, numbers))

# Функция map() возвращает объект, поддерживающий итерации, а не список. Чтобы получить из него список, необходимо результат передать в функцию list()

# Функции map() можно передать несколько последовательностей. В этом случае в функцию обратного вызова func будут передаваться сразу несколько элементов, расположенных в последовательностях на одинаковых позициях

# def func(elem1, elem2, elem3):
#     return elem1 + elem2 + elem3
#
#
# numbers1 = [1, 2, 3, 4, 5]
# numbers2 = [10, 20, 30, 40, 50]
# numbers3 = [100, 200, 300, 400, 500]
#
# new_numbers = list(map(func, numbers1, numbers2, numbers3))  #  преобразуем итератор в список
#
# print(new_numbers)

# Если в последовательностях разное количество элементов, то последовательность с минимальным количеством элементов становится ограничителем

# def func(elem1, elem2, elem3):
#     return elem1 + elem2 + elem3
#
#
# numbers1 = [1, 2, 3, 4]
# numbers2 = [10, 20]
# numbers3 = [100, 200, 300, 400, 500]
#
# new_numbers = list(map(func, numbers1, numbers2, numbers3))  #  преобразуем итератор в список
#
# print(new_numbers)

# Встроенная функция map() реализована очень гибко. В качестве последовательностей мы можем использовать: списки, строки, кортежи, множества, словари

# circle_areas = [3.56773, 5.57668, 4.31914, 6.20241, 91.01344, 32.01213]
#
# result1 = list(map(round, circle_areas, [1]*6))         # округляем числа до 1 знака после запятой
# result2 = list(map(round, circle_areas, range(1, 7)))   # округляем числа до 1,2,...,6 знаков после запятой
#
# print(circle_areas)
# print(result1)
# print(result2)

# Встроенная функция round(x, n=0) принимает два числовых аргумента x и n и округляет переданное число x до n цифр после десятичной запятой. Значением по умолчанию для n является 0



#                                                       Встроенная функция filter()

# Встроенная функция filter() имеет сигнатуру filter(func, iterable). В отличие от нашей реализации из прошлого урока она может принимать любой итерируемый объект (список, строку, кортеж, и т.д.)

# В качестве параметра func указывается ссылка на функцию, которой будет передаваться текущий элемент последовательности. Внутри функции func необходимо вернуть значение True или False. Для примера, удалим все отрицательные значения из списка
# def func(elem):
#     return elem >= 0
#
#
# numbers = [-1, 2, -3, 4, 0, -20, 10]
# positive_numbers = list(filter(func, numbers))  #  преобразуем итератор в список
#
# print(positive_numbers)

# Обратите внимание: функция filter() как и функция map() возвращает не список, а специальный объект, который называется итератором. Итераторы можно перебрать с помощью цикла for, либо преобразовать в список

# Встроенной функции filter() можно в качестве первого параметра func передать значение None. В таком случае каждый
# элемент последовательности будет проверен на соответствие значению True. Если элемент в логическом контексте возвращает значение False, то он не будет добавлен в возвращаемый результат

# true_values = filter(None, [1, 0, 10, '', None, [], [1, 2, 3], ()])
#
# for value in true_values:
#     print(value)


#                            ****************        Функция reduce()                *********

# Для использования функции reduce() необходимо подключить специальный модуль functools. Функция reduce() имеет сигнатуру reduce(func, iterable, initializer=None).
# Если начальное значение не установлено, то в его качестве используется первое значение из последовательности iterable

from functools import reduce


# def func(a, b):
#     return a + b
#
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# total = reduce(func, numbers, 0)   # в качестве начального значения 0
# print(total)

# Обратите внимание на то, что мы могли вызвать функцию так
# total = reduce(func, numbers)   # в качестве начального значения первый элемент списка numbers

# Функция reduce() во второй версии языка Python была встроенной, но в Python 3 ее решили перенести в модуль functools. Функция reduce() как и функции map() и filter() может принимать любой итерируемый объект

# from functools import reduce
#
#
# def mult(a, b):
#     return a * b
#
# numbers = [5, 2, 3]
# product = reduce(mult, numbers)
#
# print(product)


#                                       **********  Модуль operator  ********
# Чтобы не писать каждый раз функции, определяющие такие стандартные математические операции как сумма или произведение
# def sum_func(a, b):
#     return a + b
#
#
# def mult_func(a, b):
#     return a * b

# можно использовать уже реализованные функции из модуля operator

# from operator import *     #  импортируем все функции
# #
# # print(add(10, 20))         #  сумма
# # print(floordiv(20, 3))     #  целочисленное деление
# # print(neg(9))              #  смена знака
# # print(lt(2, 3))            #  проверка на неравенство <
# # print(lt(10, 8))           #  проверка на неравенство <
# # print(eq(5, 5))            #  проверка на равенство ==
# # print(eq(5, 9))            #  проверка на равенство ==
#
#
# from functools import reduce
#
#
# numbers = [5, 2]
# product = reduce(neg, numbers)
#
# print(product)

# from functools import reduce
# import operator
#
# words = ['Testing ', 'shows ', 'the ', 'presence', ', ', 'not ', 'the ', 'absence ', 'of ', 'bugs']
# numbers = [1, 2, -6, -4, 3, 9, 0, -6, -1]
#
# opposite_numbers = list(map(operator.neg, numbers))    #  смена знаков элементов списка
# concat_words = reduce(operator.add, words)             #  конкатенация элементов списка
#
# print(opposite_numbers)
# print(concat_words)

# Модуль operator реализован на языке C, поэтому функции этого модуля работают в разы быстрее, чем самописные функции в Python

# Примечание 1. Итераторы – важная концепция языка Python. Нужно помнить:
#
# итераторы можно обойти циклом for;
# итератор можно преобразовать в список или кортеж, с помощью функций list() и tuple();
# итератор можно распаковать с помощью *


# numbers = [1, 10, -9, 8, 9, 345, -32, -89, 2]
#
# map_obj = map(abs, numbers)
#
# print(*map_obj)

# Примечание 2. Если нам нужны строковые методы в виде функций, мы можем получить их через название типа str

# pets = ['alfred', 'tabitha', 'william', 'arla']
# chars = ['x', 'y', '2', '3', 'a']
#
# uppered_pets = list(map(str.upper, pets))
# capitalized_pets = list(map(str.capitalize, pets))
# only_letters = list(filter(str.isalpha, chars))
#
# print(uppered_pets)
# print(capitalized_pets)
# print(only_letters)

# Аналогично можно получить методы других типов данных в виде функций

# Примечание 4. В уроке, посвященном списочным выражениям, мы разбирали конструкции очень похожие на действие
# функций map() и filter(). Списочное выражение можно рассматривать как комбинацию фильтрации и трансформации: сначала выполняется фильтрация, затем — трансформирование
# *************
# iterable = [[1], [2], [3]]
# result = list(map(len, iterable))
# print(result)
#
# # *************
# random_list = [1, 'a', 0, False, True, '0', 7, '']
# filtered_list = list(filter(None, random_list))
# print(filtered_list)
#
# # **********
# listA = [2, 3, 4]
# listB = [3, 2, 1]
#
# result = sum(map(pow, listA, listB))
# print(result)
#
# # **********
# from operator import mul
# from functools import reduce
#
# result = reduce(mul, range(1, 6))
# print(result)
#
# # *********
# from operator import add
#
# result = list(map(add, 'abc', '1234'))
# print(result)
#
#
# # *************
# from operator import mul
#
# result = list(map(mul, ['a', 'b', 'c'], [1, 2, 3]))
# print(result)
#
# # ********
# from operator import add
# from functools import reduce
#
# result = reduce(add, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(result)