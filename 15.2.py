                                    # функции с переменным количеством аргументов

#                               Переменное количество аргументов

# def my_func(*args):
#     print(type(args))
#     print(args)
#
#
# my_func()
# my_func(1, 2, 3)
# my_func('a', 'b')
#
#
# def my_func(num, *args):
#     print(args)
#     print(num)
#
#
# my_func(17, 'Python', 2, 'C#')


#           ****************    Передача аргументов в форме списка и кортежа

# def my_sum(*args):
#     return sum(args)    # args - это кортеж
#
# print(my_sum())
# print(my_sum(1))
# print(my_sum(1, 2))
# print(my_sum(1, 2, 3))
# print(my_sum(1, 2, 3, 4))

# **********************            Получение именованных аргументов в виде словаря

# Позиционные аргументы можно получать в виде *args, причём произвольное их количество.
# Такая возможность существует и для именованных аргументов. Только именованные аргументы получаются в виде словаря, что позволяет сохранить имена аргументов в ключах.

# def my_func(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#
#
# my_func()
# my_func(a=1, b=2)
# my_func(name='Timur', job='Teacher')


# Рассмотрим определение функции, которая принимает все виды аргументов.
# def my_func(a, b, *args, name='Gvido', age=17, **kwargs):
#     print(a, b)
#     print(args)
#     print(name, age)
#     print(kwargs)
#
#
# my_func(1, 2, 3, 4, name='Timur', age=28, job='Teacher', language='Python')
# my_func(1, 2, name='Timur', age=28, job='Teacher', language='Python')
# my_func(1, 2, 3, 4, job='Teacher', language='Python')


#               ****************        Передача именованных аргументов в форме словаря

# Как и в случае позиционных аргументов, именованные можно передавать в функцию "пачкой" в виде словаря. Для этого нужно перед словарём поставить две звёздочки

# def my_func(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#
# info = {'name':'Timur', 'age':'28', 'job':'teacher'}
#
# my_func(**info)

# def print_info(name, surname, age, city, *children, **additional_info):
#     print('Имя:', name)
#     print('Фамилия:', surname)
#     print('Возраст:', age)
#     print('Город проживания:', city)
#     if len(children) > 0:
#         print('Дети:', ', '.join(children))
#     if len(additional_info) > 0:
#         print(additional_info)
#
#
# children = ['Бодхи Рансом Грин', 'Ноа Шэннон Грин', 'Джорни Ривер Грин']
# additional_info = {'height':163, 'job':'actress'}
#
# print_info('Меган', 'Фокс', 34, 'Ок-Ридж', *children, **additional_info)


#       *********************       Keyword-only аргументы

# В Python 3 добавили возможность пометить именованные аргументы функции так, чтобы вызвать функцию можно было,
# только передав эти аргументы по именам. Такие аргументы называются keyword-only и их нельзя передать в функцию в виде позиционных



# Здесь * выступает разделителем: отделяет обычные аргументы (их можно указывать по имени и позиционно) от строго именованных.
# def make_circle(x, y, radius, *, line_width=1, fill=True):
#     pass
# make_circle(10, 20, 5)                                     # x=10, y=20, radius=5,  line_width=1, fill=True
# make_circle(x=10, y=20, radius=7)                          # x=10, y=20, radius=7,  line_width=1, fill=True
# make_circle(10, 20, radius=10, line_width=2, fill=False)   # x=10, y=20, radius=10, line_width=2, fill=False
# make_circle(x=10, y=20, radius=17, line_width=3)           # x=10, y=20, radius=17, line_width=3, fill=True

# Этот пример неплохо демонстрирует подход к описанию аргументов. Первые три аргумента — координаты центра круга и радиус.
# Координаты центра и радиус присутствуют у круга всегда, поэтому обязательны и их можно не именовать.
# А вот line_width и fill — необязательные аргументы, ещё и получающие ничего не говорящие значения. Вполне логично ожидать,
# что вызов вида make_circle(10, 20, 5, 3, False) мало кому понравится! Ради ясности аргументы line_width и fill  и объявлены так, что могут быть указаны только явно через имя.


# Мы также можем объявить функцию, у которой будут только строго именованные аргументы, для этого нужно поставить звёздочку в самом начале перечня аргументов.
# def make_circle(*, x, y, radius, line_width=1, fill=True):
#     print('ok')
#
# make_circle(x=10, y=20, radius=15)                              # line_width=1, fill=True
# make_circle(x=10, y=20, radius=15, line_width=4, fill=False)

# Примечание 1. Специальный синтаксис *args и **kwargs в определении функции позволяет передавать функции переменное
# количество позиционных и именованных аргументов. При этом args и kwargs просто имена. Вы не обязаны их использовать,
# можно выбрать любые, однако среди Python программистов приняты именно эти.
#
# Примечание 2. Вы можете использовать одновременно *args и **kwargs в одной строке для вызова функции.
# В этом случае порядок имеет значение. Как и аргументы, не являющиеся аргументами по умолчанию, *args должны предшествовать и аргументам по умолчанию, и **kwargs. Правильный порядок параметров:
#
# позиционные аргументы,
# *args аргументы,
# **kwargs аргументы.
# def my_func(a, b, *args, **kwargs):

# *************
# def f(n=3):
#     return n + 7
#
#
# print(f(f(f())))


# ********
# def func(x, y, *args):
#     return len(args)
#
#
# print(func(10, 20, 30, 40, 50, 60))

# *****************
# def func(*args):
#     return max(args) + min(args)
#
#
# print(func(10, 15, *[31, 42, 5, 1], *(17, 28, 19, 100), 13, 12))


# ***************
# def count_args(*args):
#     return len(args)
#
# print(count_args())
# print(count_args(10))
# print(count_args('stepik', 'beegeek'))
# print(count_args([], (''), 'a', 12, False))

# ***********
# def sq_sum(*args):
#     return sum([el ** 2 for el in args])
#
# print(sq_sum())
# print(sq_sum(2))
# print(sq_sum(1.5, 2.5))
# print(sq_sum(1, 2, 3))
# print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

#*************
# def mean(*args):
#     sum = 0
#     count = 0
#     for el in args:
#         if type(el) is int or type(el) is float:
#             sum += el
#             count += 1
#     if count > 0:
#         return sum / count
#     else:
#         return float(sum)
#
#
# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# **********(ОТ ПОЛЬЗОВАТЕЛЯ)
# def mean(*args):
#     a = [i for i in args if type(i) in (int, float)]
#     return sum(a) / len(a) if a else 0
#
#
# # *************(ОТ ПОЛЬЗОВАТЕЛЯ)
# def mean(*args):
#     s = [float(i) for i in args if type(i) in (int, float)]
#     if len(s) > 0:
#         return sum(s)/len(s)
#     else:
#         return 0.0

# ***********
# def greet(name, *args):
#     names = [name]
#
#     for el in args:
#         names.append(el)
#
#     return 'Hello, ' + ' and '.join(names) + '!'
#
# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))
#
# # ***********(ОТ ПОЛЬЗОВАТЕЛЯ)
# def greet(name, *args):
#     return f'Hello, {" and ".join((name,) + args)}!'
#
# # **************(ОТ ПОЛЬЗОВАТЕЛЯ)
# def greet(name, *args):
#     return 'Hello, ' + ' and '.join([name, *args]) + '!'


# ****************
# def print_products(*args):
#     s = [el for el in args if type(el) is str and len(el) > 0]
#
#     if len(s) == 0:
#         print('Нет продуктов')
#     else:
#         for i in range(len(s)):
#             print(f'{i + 1}) {s[i]}')
#
#
# # **************(ОТ ПОЛЬЗОВАТЕЛЯ)
# def print_products(*args):
#     cnt = 0
#     for e in args:
#         if type(e) == str and e:
#             cnt += 1
#             print(f'{cnt}) {e}')
#     if cnt == 0:
#         print('Нет продуктов')
#
#
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
# print_products([4], {}, 1, 2, {'Beegeek'}, '')


# **************
# def info_kwargs(**kwargs):
#     for key, value in sorted(kwargs.items()):
#         print(f'{key}: {value}')
#
# # *************(ОТ ПОЛЬЗОВАТЕЛЯ)
# def info_kwargs(**kwargs):
#     [print(f'{key}: {kwargs[key]}') for key in sorted(kwargs.keys())]
#
#
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')






