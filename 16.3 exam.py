# def concat(*args, sep=' '):
#     return sep.join(map(str, args))
#
#
#
# print(concat('hello', 'python', 'and', 'stepik'))
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))
# print(concat('hello', 'python', sep='()()()'))
# print(concat('hello', sep='()'))
# print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))
#
# ***********
# from functools import reduce
# def product_of_odds(data):
#
#     return reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 1, data), 1)

# **************
# words = 'the world is mine take a look what you have started'.split()
#
# print(*list(map(lambda x: f'"{x}"', words)))

# *************
# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
#
# print(*list(filter(lambda x: str(x) != str(x)[::-1], numbers)))

# *************
# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
#
# sorted_numbers = sorted(numbers, key=lambda x: sum(x) / len(x), reverse=True)
#
# print(sorted_numbers)

# *************
# def mul7(x):
#     return x * 7
#
#
# def add2(x, y):
#     return x + y
#
#
# def add3(x, y, z):
#     return x + y + z
#
#
# def call(func, *args):
#     return func(*args)
#
# print(call(mul7, 10))
# print(call(add2, 2, 7))
# print(call(add3, 10, 30, 40))
# print(call(bool, 0))


# ***********
# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
#
# def compose(func1, func2):
#     return lambda x: func1(func2(x))
#
# print(compose(mul7, add3)(1))
# print(compose(add3, mul7)(2))
# print(compose(mul7, str)(3))
# print(compose(str, mul7)(5))


# *************
# def arithmetic_operation(operation):
#     return {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}[operation]


# add = arithmetic_operation('+')
# div = arithmetic_operation('/')
# print(add(10, 20))
# print(div(20, 5))

# В ОДНУ СТРОКУ

# print(*sorted(input().split(), key=lambda x: x.lower()))


# ГЕМАТРИЯ СЛОВА

# words = sorted([input() for _ in range(int(input()))])
#
# def gem(word):
#     total = 0
#     for i in word:
#         total += ord(i.upper()) - ord('A')
#     return total
#
#
# print(*sorted(words, key=gem), sep='\n')


# СОРТИРОВКА IP-АДРЕСОВ

# ip_list = [[int(num) for num in input().split('.')] for _ in range(int(input()))]
# print(ip_list)

# def check_ip(ip):
#     # res = list(map(lambda x: x[0] * 256 ** 3 + x[1] * 256 ** 2 + 1 * 256 ** 1 + 2 * 256 ** 0, ip))
#     # return res
#     # return lambda ip: ip[0] * 256 ** 3 + ip[1] * 256 ** 2 + 1 * 256 ** 1 + 2 * 256 ** 0
#
#     print(ip)

# print(check_ip(ip_list))

# print(*sorted(ip_list, key=check_ip), sep='\n')


# ip_list = [[int(num) for num in input().split('.')] for _ in range(int(input()))]
# print(ip_list)
#
# ip_list.sort()
#
# new_list = []
# for el in ip_list:
#     cur_list = []
#     for num in el:
#         cur_list.append(str(num))
#     new_list.append('.'.join(cur_list))
#
# print(*new_list, sep='\n')


# **********
# n = int(input())
# ip_list = [input() for _ in range(n)]
# print(ip_list)
#
# k = lambda x: list(map(int, x.split('.'), ip_list))
# #
# print(*sorted(ip_list, key=k), sep='\n')



# x = ['1', '2', '3']
#
# y = '.'.join(x)
# print(y)








