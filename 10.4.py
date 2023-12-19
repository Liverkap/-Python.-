
# СЛОВАРЬ ПРОГРАММИСТА

# my_dict = {}
#
# for _ in range(int(input())):
#     key, value = input().split(': ')
#     my_dict[key.lower()] = value
#
# for i in range(int(input())):
#     print(my_dict.get(input().lower(), 'Не найдено'))
#
#
# # СЛОВАРЬ ПРОГРАММИСТА (ОТ ПОЛЬЗОВАТЕЛЯ)
# d = {k.lower(): v for _ in range(int(input())) for k, v in [input().split(': ', 1)]}
# print(*(d.get(input().lower(), 'Не найдено') for _ in range(int(input()))), sep='\n')


# АННАГРАММЫ 1

# a, b = input(), input()
#
# my_dict_a = {}
# my_dict_b = {}
#
# for el in a:
#     my_dict_a[el] = my_dict_a.get(el, 0) + 1
#
# for el in b:
#     my_dict_b[el] = my_dict_b.get(el, 0) + 1
#
# if my_dict_a == my_dict_b:
#     print('YES')
# else:
#     print('NO')

# АННАГРАММЫ 1(ОТ ПОЛЬЗОВАТЕЛЯ)(ЧЕРЕЗ ЗАМЕНУ КЛЮЧА)
# a1 = tuple(sorted(input()))
# a2 = tuple(sorted(input()))
# d = {a1: "NO", a2: "YES"}
# print(d[a1])


# АННАГРАММЫ 2

# a = [el.lower().strip('.,!?:;-') for el in input().split()]
# b = [el.lower().strip('.,!?:;-') for el in input().split()]
#
# my_dict_a = {}
# my_dict_b = {}
#
# for i in range(len(a)):
#     for el in a[i]:
#         my_dict_a[el] = my_dict_a.get(el, 0) + 1
#
# for i in range(len(b)):
#     for el in b[i]:
#         my_dict_b[el] = my_dict_b.get(el, 0) + 1
#
# if my_dict_a == my_dict_b:
#     print('YES')
# else:
#     print('NO')

# АННАГРАММЫ 2 (ИСПОЛЬЗУЕМ МЕТОД JOIN)
# a = [el.lower().strip('.,!?:;-') for el in input().split()]
# b = [el.lower().strip('.,!?:;-') for el in input().split()]
#
# my_dict_a = {}
# my_dict_b = {}
#
# for el in ''.join(a):
#     my_dict_a[el] = my_dict_a.get(el, 0) + 1
#
# for el in ''.join(b):
#     my_dict_b[el] = my_dict_b.get(el, 0) + 1
#
# if my_dict_a == my_dict_b:
#     print('YES')
# else:
#     print('NO')


# СЛОВАРЬ СИНОНИМОВ

# synonyms_1 = {}
# synonyms_2 = {}
#
# for _ in range(int(input())):
#     key, value = input().split()
#     synonyms_1[key] = value
#     synonyms_2[value] = key
#
# syn = input()
#
# if syn in synonyms_1:
#     print(synonyms_1[syn])
# else:
#     print(synonyms_2[syn])
#
# # СЛОВАРЬ СИНОНИМОВ (АНАЛОГИЧНО МОЕМУ РЕШЕНИЮ, НО СОБИРАЕМ ВСЕ В 1 СЛОВАРЬ)
# words = {}
# for _ in range(int(input())):
#     a, b = input().split()
#     words[a], words[b] = b, a
# print(words[input()])



# ТЕЛЕФОННАЯ КНИГА

# my_dict = {}
#
# for _ in range(int(input())):
#     key, value = input().split()
#     my_dict.setdefault(value.lower(), []).append(key)
#
#
# for _ in range(int(input())):
#     k = input().lower()
#     if k in my_dict:
#         print(*my_dict[k])
#     else:
#         print('абонент не найден')


# СЕКРЕТНОЕ СЛОВО

word = input()

my_dict_1 = {}

for _ in range(int(input())):
    key, value = input().split()
    my_dict_1[int(value)] = key.strip(':')


for ch in word:
    print(my_dict_1.get(word.count(ch)), end='')











