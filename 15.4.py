#                               функции как объекты

# До сих пор мы рассматривали функции как совершенно отдельный элемент языка со своим синтаксисом и механизмом работы.
# Но, оказывается, функции также что-то вроде особого типа объектов. Бывают числа, строки, списки, кортежи, словари,
# множества. А бывают — функции. У каждого из этих типов есть свои операции, свой синтаксис, но все они — объекты


# num = 17
# numbers = [1, 2, 3]
# colors = (1, 2, 3)
# name = 'Python'
#
# print(type(num))
# print(type(numbers))
# print(type(colors))
# print(type(name))


# Поскольку функции тоже объекты, работать с ними можно и как с объектами: записывать их в переменные, передавать в качестве аргументов другим функциям, возвращать из функций и т.д.

# def hello():
#     print('Hello from function')
#
#
# func = hello     #  присваиваем переменной func функцию hello
# func()           #  вызываем функцию
#
#
# writeln = print            # как в языке Pascal 😀
#
# writeln('Hello world!')
# writeln('Python')

# Представим себе ситуацию, когда необходимо выполнить некую функцию, если задано имя команды.
# Для простоты предположим, если пришла команда start — надо выполнить функцию start(), если команда stop — функцию stop(), если команда pause — функцию pause().

# def start():
#     # тело функции start
#     pass
#
#
# def stop():
#     # тело функции stop
#     pass
#
#
# def pause():
#     # тело функции pause
#     pass
#
#
# command = input()  # считываем название команды
#
# if command == 'start':
#     start()
# elif command == 'stop':
#     stop()
# elif command == 'pause':
#     pause()

# Однако если команд будет много или если их количество будет увеличиваться, то оператор if получится слишком громоздким. В этом случае можно создать словарь, где ключом служит название команды, а значением — соответствующая функция

# def start():
#     # тело функции start
#     pass
#
#
# def stop():
#     # тело функции stop
#     pass
#
#
# def pause():
#     # тело функции pause
#     pass
#
#
# commands = {'start': start, 'stop': stop, 'pause': pause}  # словарь соответствия команда → функция
#
# command = input()  # считываем название команды
#
# commands[command]()  # вызываем нужную функцию через словарь по ключу


#               *****************       Функции в качестве аргументов других функций*************

# Возможность присваивать имя функции переменной позволяет, в частности, передавать имя функции аргументом другой функции. Это доступно во многих языках, но в Python проще, благодаря его гибкой типизации.

# Например, есть программная функция построения графика для заданной математической функции. Если нужно строить графики многих математических функций, то каждый раз придется писать новую функцию, или модифицировать имеющуюся.
#
# Но логика построения графика функции практически не зависит от типа математической функции, поэтому можно рассматривать математическую функцию как аргумент программной функции построения графика. Определим функцию plot(), которая принимает
# 3
# 3 аргумента: f – функцию, для которой хотим построить график, и a, b – границы диапазона построения графика.

# При запуске функции plot() мы можем указать, для какой именно функции строим график. Например, пусть у нас есть следующие математические функции:

# def plot(f, a, b):
#     pass
#
# def square_add_one(x):
#     return x * x + 1
#
#
# def cube_add_square(x):
#     return x ** 3 + x ** 2
#
# plot(square_add_one, 1, 10)

# Функции, способные в качестве аргумента принимать или/и возвращать другие функции, называются функциями высшего порядка.!!!!!!!!!


#                   **********************      Встроенные функции, принимающие функции в качестве аргументов       ***
# numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]
#
# print(max(numbers))
# print(min(numbers))
# print(sorted(numbers))
#
# # Но что, если мы хотим написать код для поиска максимального по модулю элемента списка numbers? И вообще, сравнивать элементы не стандартным способом, а более специфическими?
# #
# # На этот случай все выше перечисленные встроенные функции могут принимать необязательный аргумент key – функцию,
# # определяющую условия сравнения элементов. Другими словами, значение key должно быть функцией, принимающей один аргумент и возвращающей на его основе ключ для сравнения
#
# # Функция, определяющая условия сравнения элементов, называется компаратор (compare – сравнивать)
# # Встроенные функции min(), max(), sorted() – функции высшего порядка, так как принимают в качестве аргумента функцию сравнения элементов.
#
# numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]
#
# print(max(numbers, key=abs))        #  указываем функцию abs в качестве компаратора
# print(min(numbers, key=abs))        #  указываем функцию abs в качестве компаратора
# print(sorted(numbers, key=abs))     #  указываем функцию abs в качестве компаратора

# При использовании встроенной функции sorted() (или списочного метода sort()) сортировка пройдет по первым значениям пар кортежа, а в случае их совпадения – по вторым.
# points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]
#
# points.sort()    #  сортируем список точек на месте
#
# print(points)
#
# # ***********
# def compare_by_second(point):
#     return point[1]
#
#
# def compare_by_sum(point):
#     return point[0] + point[1]
#
#
# points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]
#
# print(sorted(points, key=compare_by_second))   # сортируем по второму значению кортежа
# print(sorted(points, key=compare_by_sum))



#           ******************      Функции в качестве возвращаемых значений других функций     **********

# Рассмотрим код, где функция generator() возвращает функцию hello() в качестве результата своей работы.
# def generator():
#     def hello():
#         print('Hello from function!')
#     return hello
#
# func = generator()
# func()

#  В Python можно определять функцию внутри функции, ведь функция это объект.

# def generator_square_polynom(a, b, c):
#     def square_polynom(x):
#         return a * x**2 + b * x + c
#
#     return square_polynom
#
# f = generator_square_polynom(a=1, b=2, c=1)
# g = generator_square_polynom(a=2, b=0, c=-3)
# h = generator_square_polynom(a=-3, b=-10, c=50)
#
# print(f(1))
# print(g(2))
# print(h(-1))

# Обратите внимание на то, что внутренняя функция square_polynom() использует параметры внешней функции generator_square_polynom(). Такую вложенную функцию называют замыканием.
#
# Замыкания – вложенные функции, ссылающиеся на переменные, объявленные вне определения этой функции, и не являющиеся её параметрами.

# Примечание 1. Функция sorted() и списочный метод sort() помимо необязательного аргумента key принимают еще аргумент reverse,
# который по умолчанию имеет значение False, что соответствует сортировке по возрастанию. Если значение reverse установить в True, произойдет сортировка по убыванию.

# Примечание 2. Сортировка при помощи функции sorted() и списочного метода sort() стабильна, то есть гарантирует неизменность взаиморасположения равных между собой элементов.

# def comparator(item):
#     return item[0]
#
#
# data = [('red', 1), ('blue', 2), ('green', 5), ('blue', 1)]
# data.sort(key=comparator)   # сортируем по первому полю
#
# print(data)
#
# Примечание 3. Функции max() и min() возвращают первый максимальный или минимальный элемент, если таковых несколько.
#
# Примечание 4. Надо четко понимать что сделает код print(input()) и почему это отличается от print(input).
# Код print(input()) запросит у пользователя текст и тут же его напечатает, т.к. функция input() будет вызвана.
# Код print(input) выдаст нам текстовое представление этой функции: строку built-in function input, которая поясняет, что input — встроенная функция языка.

# ***********
# s1 = 'python'
# s2 = 'stepicon'
# s3 = 'beegeek'
#
# print(min(s1, s2, s3))
# print(max(s1, s2, s3))
#
# # ***********
# s1 = 'python'
# s2 = 'stepicon'
# s3 = 'beegeek'
#
# print(min(s1, s2, s3, key=len))
# print(max(s1, s2, s3, key=len))
#
# # **********
# def f(x):
#     return x**2
#
#
# g = f
# print(f(3), g(5))
#
# # **********
# def f(x):
#     return x**2
#
#
# def g(x):
#     return x**3
#
#
# funcs = [f, g]
# print(funcs[0](5), funcs[1](5))
#
# # *********
# def comparator(pair):
#     return pair[1]
#
#
# pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
# pairs.sort(key=comparator)
# print(pairs)
#
# # ***********
# def comparator(pair):
#     return pair[0] + pair[1]
#
#
# pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
# pairs.sort(key=comparator, reverse=True)
# print(pairs)
#
# # **********
# words = ['this', 'is', 'a', 'test', 'of', 'sorting']
# words.sort(key=len)
# print(words)
#
# # ************
# def f1(x):
#     return 2*x+1
#
#
# def f2(x):
#     return x**2
#
#
# def f3(x):
#     return -x**2+1
#
#
# def f4(x):
#     return x-3
#
#
# funcs = [f1, f2, f3, f4]
# i = int(input())
# print(funcs[i](2))

# **********
# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2),
#            (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
#
# def averange(x):
#     return sum(x) // len(x)
#
#
# print(min(numbers, key=averange))
# print(max(numbers, key=averange))
#
# # *************(ОТ ПОЛЬЗОВАТЕЛЯ)
# from statistics import mean
# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
#
# print(*(func(numbers, key=mean) for func in (min, max)), sep='\n')

# *************
# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
#
# def compare(pair):
#     return (pair[0] ** 2 + pair[1] ** 2) ** 0.5
#
# points.sort(key=compare)
#
# print(points)

# *************
# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
#
#
# def compare(pair):
#     return min(pair) + max(pair)
#
#
# print(sorted(numbers, key=compare))

# *************(ОТ ПОЛЬЗОВАТЕЛЯ)
# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
#
# def com(x):
#     return min(x) + max(x)
#
# numbers.sort(key=com)
#
# print(numbers)


# СОРТИРУЙ КАК ХОЧЕШЬ
# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
#
# x = int(input())
# def compare(athlet):
#     return athlet[x - 1]
#
# athletes.sort(key=compare)
#
# for el in athletes:
#     print(*el)
#
# # *********(ОТ ПОЛЬЗОВАТЕЛЯ)(ЧЕРЕЗ ЗАМЫКАНИЕ)
# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
#
# def gen_comparator(field=1):
#     def comp(seq):
#         return seq[field - 1]
#     return comp
#
# cmp = gen_comparator(int(input()))
# athletes.sort(key=cmp)
# for a in athletes:
#     print(*a)


# МАТЕМАТИЧЕСКИЕ ФУНКЦИИ
# from math import sin
#
# def get_num_square(num):
#     return num ** 2
#
# def get_num_cube(num):
#     return num ** 3
#
# def get_square_root_of_num(num):
#     return num ** 0.5
#
# def get_num_abs(num):
#     return abs(num)
#
# def get_sin_of_num(num):
#     return sin(num)
#
# func = {'квадрат': get_num_square, 'куб': get_num_cube, 'корень': get_square_root_of_num, 'модуль': get_num_abs, 'синус': get_sin_of_num}
#
# num, function_name = int(input()), input()
#
# print(func[function_name](num))

# МАТЕМАТИЧЕСКИЕ ФУНКЦИИ(ОТ ПОЛЬЗОВАТЕЛЯ)
# import math
#
# def pwr(p):
#   def numpower(n):
#     return n**p
#   return numpower
#
# commands = {"квадрат": pwr(2), "куб": pwr(3), "корень": pwr(0.5), "модуль": abs, "синус": math.sin}
#
# n = int(input())
# command = input()
# print(commands[command](n))

# ИНТЕРЕСНАЯ СОРТИРОВКА-1

# def compare(num):
#     sum = 0
#     for ch in num:
#         sum += int(ch)
#
#     return sum
#
# numbers = input().split()
#
# print(*sorted(numbers, key=compare))


# ИНТЕРЕСНАЯ СОРТИРОВКА-1 (ОТ ПРЕПОДАВАТЕЛЯ)(СУММА ЧЕРЕЗ СПИСОК)
# def comparator(n):
#     return sum([int(i) for i in str(n)])
#
# numbers = [int(i) for i in input().split()]
#
# print(*sorted(numbers, key=comparator))


# ИНТЕРЕСНАЯ СОРТИРОВКА-2

# def compare_sum(num):
#     return sum([int(ch) for ch in str(num)])
#
#
# numbers = sorted([int(num) for num in input().split()])
#
# print(*sorted(numbers, key=compare_sum))
#

# # ИНТЕРЕСНАЯ СОРТИРОВКА-2(ОТ ПОЛЬЗОВАТЕЛЯ)
# def comparator(n):
#     return sum([int(i) for i in str(n)]), n
#
# numbers = [int(i) for i in input().split()]
#
# print(*sorted(numbers, key=comparator))




