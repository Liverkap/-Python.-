
# МИНУТКА ГЕНЕТИКИ

# my_dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
#
# dnk = input()
#
# for ch in dnk:
#     print(my_dict[ch], end='')


# ПОРЯДКОВЫЙ НОМЕР

# my_list = input().split()
# my_dict = {}
# for el in my_list:
#     if el not in my_dict:
#         my_dict[el] = 1
#         print(my_dict[el], end=' ')
#     else:
#         my_dict[el] += 1
#         print(my_dict[el], end=' ')


# SCRABBLE GAME
# my_dict = {1: 'AEILNORSTU', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# word = input()
# res = 0
# for key, value in my_dict.items():
#     for ch in word:
#         if ch in value:
#             res += key
#
# print(res)


# СТРОКА ЗАПРОСА

# def build_query_string(params):
#     my_list = []
#     for key, value in params.items():
#         my_list.append(str(key) + '=' + str(value))
#
#     return '&'.join(sorted(my_list))
#
# print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))


# СЛИЯНИЕ СЛОВАРЕЙ

# def merge(values):
#     my_dict = {}
#     for el in values:
#         for key, value in el.items():
#             my_dict.setdefault(key, set()).add(value)
#
#     return my_dict
#
#
# result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
# print(result)

# ОПАСНЫЙ ВИРУС

# commands = {'write': 'W', 'read': 'R', 'execute': 'X'}
#
# files = {}
#
# for _ in range(int(input())):
#     s = input().split()
#     files.setdefault(s[0], s[1:])
#
# for _ in range(int(input())):
#     s = input().split()
#     if commands[s[0]] in files[s[1]]:
#         print('OK')
#     else:
#         print('Access denied')


# ПОКУПКИ В ИНТЕРНЕТ-МАГАЗИНЕ

# my_dict = {}
#
# for _ in range(int(input())):
#     name, item, count = input().split()
#     if name not in my_dict.keys():
#         my_dict[name] = my_dict.setdefault(name, {item: int(count)})
#     else:
#         if item not in my_dict[name]:
#             my_dict[name].update({item: int(count)})
#         else:
#             my_dict[name][item] = my_dict[name].get(item) + int(count)
#
#
# for key, value in sorted(my_dict.items()):
#     print(key + ':')
#     for key2, value2 in sorted(my_dict[key].items()):
#         print(key2, value2)


# ПОКУПКИ В ИНТЕРНЕТ-МАГАЗИНЕ (ОТ ПОЛЬЗОВАТЕЛЯ)
data = {}

for _ in range(int(input())):
    name, product, count = input().split()
    data.setdefault(name, {})
    data[name][product] = data[name].get(product, 0) + int(count)

for person, products in sorted(data.items()):
    print(f'{person}:')
    for product, count in sorted(products.items()):
        print(product, count)








