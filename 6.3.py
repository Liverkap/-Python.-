#       *Перебор кортежей*

# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# for i in range(len(numbers)):
#     print(numbers[i])
#
#
# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# for num in numbers:
#     print(num)

# Можно использовать распаковку
# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# languages = ('Python', 'C++', 'Java')
#
# print(*numbers)
# print(*languages, sep='\n')



# Сравнение кортежей

# print((1, 8) == (1, 8))
# print((1, 8) != (1, 10))
# print((1, 9) < (1, 2))
# print((2, 5) < (6,))
# print(('a', 'bc') > ('a', 'de'))


# Сортировка кортежей
#
# not_sorted_tuple = (34, 1, 8, 67, 5, 9, 0, 23)
# print(not_sorted_tuple)
#
# sorted_tuple = tuple(sorted(not_sorted_tuple))
# print(sorted_tuple)


# Для сортировки кортежа можно воспользоваться явным преобразованием в список и использовать метод sort()
# not_sorted_tuple = ('cc', 'aa', 'dd', 'bb')
# tmp = list(not_sorted_tuple)
# tmp.sort()
#
# sorted_tuple = tuple(tmp)
# print(sorted_tuple)


# Преобразование кортежа в строку и наоборот

# notes = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')
# string1 = ''.join(notes)
# string2 = '.'.join(notes)
#
# print(string1)
# print(string2)

# poets = [
#     ('Тургенев', 14),
#     ('Есенин', 13),
#     ('Маяковский', 28),
#     ('Фет', 15),
#     ('Лермонтов', 20)]
#
# for i in range(len(poets)):
#     for j in range(i+1, len(poets)):
#         if poets[i] > poets[j]:
#             poets[i], poets[j] = poets[j], poets[i]
#
# print(poets[0])
# print(poets[-1])

# x = ('Тургенев', 14)
# y = ('Есенин', 13)
# print(x > y)


# data = 'Python для продвинутых!'
#
# print(tuple(data))


# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# x = list(poet_data)
# x[2] = 'Москва'
# poet_data = tuple(x)
#
# print(poet_data)
#
# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# poet_data = poet_data[:-1] + ('Москва',)
#
# print(poet_data)


# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
#
# my_list = []
#
# for i in range(len(numbers)):
#     total = 0
#     seq = sum(numbers[i]) / len(numbers[i])
#     my_list.append(seq)
#
# print(my_list)
#
#
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
#
# print([sum(i) / len(i) for i in numbers])


# ВЕРШИНА ПАРАБОЛЫ

# a, b, c = (int(input()) for _ in range(3))
#
# res = (-b / (2 * a), (4 * a * c - b ** 2)/(4 * a))
#
# print(res)
#
#
# # ВЕРШИНА ПАРАБОЛЫ (ОТ ПОЛЬЗОВАТЕЛЯ)
# def parabola_vertex(a, b, c):
#     x = -(b / (2 * a))
#     y = (4 * a * c - b**2) / (4 * a)
#     return x, y
#
#
# print(parabola_vertex(int(input()), int(input()), int(input())))


# КОНКУРСНЫЙ ОТБОР

# n = int(input())
#
# my_tpl = tuple([tuple(input().split()) for _ in range(n)])
#
# for el in my_tpl:
#     print(*el)
#
# print()
#
# for i in range(len(my_tpl)):
#     if int(my_tpl[i][1]) > 3:
#         print(*my_tpl[i])


# КОНКУРСНЫЙ ОТБОР (ОТ ПРЕПОДАВАТЕЛЯ)
# students = [tuple(input().split()) for _ in range(int(input()))]
#
# for student in students:
#     print(*student)
#
# print()
#
# for name, grade in students:
#     if int(grade) > 3:
#         print(name, grade)

# УПАКОВКА КОРТЕЖЕЙ - Упаковкой кортежа называют присваивание его какой-либо переменной

# tuple1 = (1, 2, 3)
# tuple2 = ('b',)
# tuple3 = ('red', 'green', 'blue', 'cyan')
#
# print(type(tuple1))
# print(type(tuple2))
# print(type(tuple3))
#
# tuple1 = 1, 2, 3
# tuple2 = 'b',
#
# print(type(tuple1))
# print(type(tuple2))


# РАСПАКОВКА КОРТЕЖЕЙ - присвоить значения элементов кортежа отдельным переменным, называется распаковкой кортежа

# colors = ('red', 'green', 'blue', 'cyan')
#
# (a, b, c, d) = colors
# print(a)
# print(b)
# print(c)
# print(d)
#
# a, b, c, d = colors
# print(a)
# print(b)
# print(c)
# print(d)
#
# # если необходимо получить лишь какие-то отдельные значения, то в качестве "ненужных" переменных позволено использовать символ нижнего подчеркивания _
#
# colors = ('red', 'green', 'blue')
# a, b, _ = colors
#
# print(a)
# print(b)


#       * при распаковке кортежей
# Есть способ собрать сразу несколько значений в одну переменную. Это делается при помощи звездочки перед именем переменной

# a, b, *tail = 1, 2, 3, 4, 5, 6
# print(tail)
#
# a, b, *tail = 1, 2, 3
#
# print(tail)

# Звездочка может быть только у одного аргумента, но НЕобязательно у последнего.
# *names, surname = ('Стефани', 'Джоанн', 'Анджелина', 'Джерманотта')
#
# print(names)
# print(surname)
#
# # Аргумент со звездочкой может стоять и посередине.
# singer = ('Freddie', 'Bohemian Rhapsody', 'Killer Queen', 'Love of my life', 'Mercury')
#
# name, *songs, surname = singer
#
# print(name)
# print(songs)
# print(surname)


# Если вы хотите распаковать единственное значение в кортеже, после имени переменной должна идти запятая.
# a = 1,      # не распаковка, а просто присвоение
# b, = 1,     # распаковка
#
# print(a)
# print(b)


# Распаковывать можно не только кортеж, правая сторона может быть любой последовательностью (кортеж, строка или список).

# info = ['timur', 'beegeek.org']
# user, domain = info    # распаковка списка
#
# print(user)
# print(domain)
#
# a, b, c, d = 'math'    # распаковка строки
#
# print(a)
# print(b)
# print(c)
# print(d)


# Помимо метода split() строковый тип данных содержит метод partition(). Метод partition() принимает на вход один
# аргумент sep, разделяет строку при первом появлении sep и возвращает кортеж, состоящий из трех элементов: часть перед
# разделителем, сам разделитель и часть после разделителя. Если разделитель не найден, то кортеж содержит саму строку,
# за которой следуют две пустые строки

# s1 = 'abc-de'.partition('-')
# s2 = 'abc-de'.partition('.')
# s3 = 'abc-de-fgh'.partition('-')
#
# print(s1)
# print(s2)
# print(s3)


# С использованием кортежей многие алгоритмы приобретают достаточно краткую форму.
# Например, вычисление чисел Фибоначчи может выглядеть следующим образом:

# n = int(input())
# f1, f2 = 1, 1
# for i in range(n):
#     print(f1)
#     f1, f2 = f2, f1 + f2


# points = [('матан', 100), ('линал', 98), ('ангем', 90)]
#
# subject, value = points[1]
#
# print(subject, value)


# ПОСЛЕДОВАТЕЛЬНОСТЬ ТРИБОНАЧЧИ

# n = int(input())
#
# f1, f2, f3 = 1, 1, 1
#
# for _ in range(n):
#     print(f1, end=' ')
#     f1, f2, f3 = f2, f3, f2 + f3