#                                           функции высшего порядка

# Как уже сказано, функции, которые принимают или/и возвращают другие функции, называются функциями высшего порядка

# def high_order_function(func):     # функция высшего порядка, так как принимает функцию
#     return func(3)
#
#
# def double(x):                     # обычная функция = функция первого порядка
#     return 2*x
#
#
# def add_one(x):                    # обычная функция = функция первого порядка
#     return x + 1
#
# print(high_order_function(double))
# print(high_order_function(add_one))

#           *************       Функции высшего порядка для обработки набора данных         *******

# Часто функции высшего порядка используются для обработки наборов данных. Рассмотрим три важные функции высшего порядка:

# map();
# filter();
# reduce().

# Функции высшего порядка map(), filter() и reduce() довольно широко распространены в функциональном программировании и часто применяются программистами.


#           **************      Функция map()       ***

# def f(x):
#     return x**2     # тело функции, которая преобразует аргумент x
#
#
# old_list = [1, 2, 4, 9, 10, 25]
# new_list = []
# for item in old_list:
#     new_item = f(item)
#     new_list.append(new_item)
#
# print(old_list)
# print(new_list)

# Несложно понять, что цикл будет выглядеть одинаково практически во всех случаях. Меняться будет только преобразование, то есть применяемая функция f(). Так почему бы не обобщить код, чтобы функция была параметром? Так и сделаем:
# def map(function, items):
#     result = []
#     for item in items:
#         new_item = function(item)
#         result.append(new_item)
#
#     return result
#
# # Теперь мы можем совершать преобразования, используя функцию высшего порядка map()
# def square(x):
#     return x**2
#
#
# def cube(x):
#     return x**3
#
#
# numbers = [1, 2, -3, 4, -5, 6, -9, 0]
#
# strings = map(str, numbers)        # используем в качестве преобразователя - функцию str
# abs_numbers = map(abs, numbers)    # используем в качестве преобразователя - функцию abs
#
# squares = map(square, numbers)     # используем в качестве преобразователя - функцию square
# cubes = map(cube, numbers)         # используем в качестве преобразователя - функцию cube
#
# print(strings)
# print(abs_numbers)
# print(squares)
# print(cubes)
#
# # Функция называется "map" то есть "отобразить". Название пришло из математики, где так называется функция, отображающая одно множество значений в другое путём преобразования всех элементов с помощью некой трансформации
#
# # Реализованную нами функцию map() можно использовать как альтернативную возможность для преобразования типов элементов любого списка. Раньше мы решали такую задачу с помощью списочных выражений. Теперь можем использовать и функцию map()
#
# strings = ['10', '12', '-4', '-9', '0', '1', '23', '100', '99']
#
# numbers1 = [int(c) for c in strings]  # используем списочное выражение для преобразования
# numbers2 = map(int, strings)          # используем функцию map() для преобразования
#
# print(numbers1)
# print(numbers2)
#
# #                   ********************        Цепочки преобразований      ************
#
# # Мы также можем строить цепочки преобразований, несколько раз вызывая функцию map().
# #
# # Приведенный ниже код при условии, что функция map() определена, как указано выше:
#
# numbers = ['-1', '20', '3', '-94', '65', '6', '-970', '8']
#
# new_numbers = map(abs, map(int, numbers))
#
# print(new_numbers)


#                       *****************       Функция filter()        *********

# Другая популярная задача при работе со списками: отобрать часть элементов списка по определенному критерию. Функция высшего порядка для решения такой задачи называется filter()
# Функция-критерий, которая возвращает значение True или False, называется предикатом

# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)  # добавляем элемент item если функция function вернула значение True
#
#     return result
#
# # Наша функция filter() применяет предикат function к каждому элементу и добавляет в итоговый список только те элементы, для которых предикат вернул True.
# #
# # Например, чтобы из исходного списка чисел получить список с элементами, большими 10, можно написать такой код
#
# def is_greater10(num):  # функция возвращает значение True если число больше 10 и False в противном случае
#     return num > 10
#
#
# numbers = [12, 2, -30, 48, 51, -60, 19, 10, 13]
#
# large_numbers = filter(is_greater10, numbers)  #  список large_numbers содержит элементы, большие 10
#
# print(large_numbers)
#
# def is_odd(num):
#     return num % 2
#
#
# def is_word_long(word):
#     return len(word) > 6
#
#
# numbers = list(range(15))
# words = ['В', 'новом', 'списке', 'останутся', 'только', 'длинные', 'слова']
#
# odd_numbers = filter(is_odd, numbers)
# large_words = filter(is_word_long, words)
#
# print(odd_numbers)
# print(large_words)

#                   ********************            Функция reduce()                *******

# Реализованные нами функции map() и filter() работали с отдельными элементами списка независимо.
# Но встречаются циклы с агрегацией результата — формированием одного результирующего значения при комбинации элементов с использованием аргумента-аккумулятора

# numbers = [1, 2, 3, 4, 5]
#
# total = 0
# product = 1
#
# for num in numbers:
#     total += num
#     product *= num
#
# print(total)
# print(product)
#
# # Несложно понять, что этот цикл будет выглядеть одинаково практически во всех случаях. Меняться будет только начальное
# # значение аккумулятора (0 для суммы, 1 для произведения и т.д.) и операция, которая комбинирует элемент и аккумулятор. Так почему бы не обобщить этот код? Так и сделаем
#
# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#
#     return acc
#
# def add(x, y):
#     return x+y
#
#
# def mult(x, y):
#     return x*y
#
#
# numbers = [1, 2, 3, 4, 5]
#
# total = reduce(add, numbers, 0)
# product = reduce(mult, numbers, 1)
#
# print(total)
# print(product)
#
#
# Примечание 1
# Каждая функция имеет меньшую мощность, чем цикл for. Цикл for позволяет гибко управлять процессом итерации, мы можем
# использовать даже команды break и continue. Возникает резонный вопрос: зачем нужны отдельные функции, когда можно обойтись циклом?
#
# Во-первых, такие функции — часть функционального подхода.
#
# Во-вторых, каждая такая функция делает единственную работу, что значительно упрощает рассуждение о коде, его чтение и написание.
# Взглянув на имя функции, можно понять, что filter() отфильтрует, а map() преобразует элементы. Более того, по построению
# функция filter() не меняет элементы, а лишь отбрасывает их часть. А функция map() меняет значение элементов, но не меняет их количество и позиции.
#
# Примечание 2. В математике определенная нами функция reduce() называется левая свёртка (left fold), по сути, мы
# сворачиваем список в одно значение, начиная слева. Существует ещё и правая свёртка (right fold). В большинстве случаев обе свёртки дают одинаковый результат, если применяемая операция ассоциативна.




# ****************
# def high_order_function(func):
#     return func(10)
#
#
# def square(x):
#     return x**2
#
#
# def minus_one(x):
#     return x - 1
#
#
# num1 = high_order_function(square)
# num2 = high_order_function(minus_one)
#
# print(num1*num2)

# *******
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'deified', 'bbbbb', 'mother', 'surface', 'sister']
#
# words_len = map(len, words)
# print(max(words_len))

# ***********
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
# def predicate(word):
#     return word == word[::-1]
#
#
# words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'language', 'deified', 'bbbbb', 'mother', 'sister', 'surface', '1234321']
# filtered = filter(predicate, words)
# print(len(filtered))

# **************
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]
#
# var1 = max(numbers, key=abs)
# var2 = min(map(abs, numbers))
# print(var1)
# print(var2)
#
# print(var1 + var2)


# **************
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
#
# def round_up(num):
#     return round(num, 2)
#
# print(*map(round_up, numbers), sep='\n')

# ******************
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434,
#            1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289,
#            1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013,
#            898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336,
#            1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
# #
# def is_reminder_two(num):
#     return 99 < num < 1000 and num % 5 == 2
#
#
# def cube(num):
#     return num ** 3
#
# new_numbers = filter(is_reminder_two, numbers)
# cubes = map(cube, new_numbers)
#
# print(*cubes, sep='\n')
#
# # ************* (ОТ ПОЛЬЗОВАТЕЛЯ)
# def numb(num):
#     return 99 < num < 1000 and num % 5 == 2
#
# def cube(num):
#     return num**3
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
#
# print(*map(cube, filter(numb, numbers)), sep='\n')


# ****************
# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35,
#            11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36,
#            72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35,
#            7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
#
# def add(x, y):
#     return x + y ** 2
#
# def square(num):
#     return num ** 2
# #
# total = reduce(add, numbers, 0)
#
# print(total)
#
# # ****************(С ПОМОЩЬЮ MAP() и SUM())
#
# new_numbers = list(map(square, numbers))
# total_new_numbers = sum(new_numbers)
#
# print(total_new_numbers)


# ************
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270,
#            219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35,
#            152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5,
#            187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35,
#            211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2,
#            79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234,
#            10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
#
#
# def is_reminded_of_num(num):
#     return 9 < abs(num) < 100 and abs(num) % 7 == 0
#
#
# def add(num):
#     return num ** 2
#
#
# total = sum(map(add, filter(is_reminded_of_num, numbers)))
#
# print(total)


# **************
# def func_apply(function, items):
#     total = []
#     for el in items:
#         total.append(function(el))
#
#     return total
#
# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
#
# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))
#
#
# # ************ (ОТ ПОЛЬЗОВАТЕЛЯ)
# def func_apply(func, arr):
#     return [func(x) for x in arr]
#
# # ************(ОТ ПОЛЬЗОВАТЕЛЯ)(ЧЕРЕЗ ВСТРОЕННЫЙ MAP())
# def func_apply(func, ar):
#     return list(map(func, ar))
