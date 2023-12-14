#                    ****************************  МЕТОДЫ СЛОВАРЕЙ *******************
# метод items() – возвращает словарные пары ключ: значение, как соответствующие им кортежи;
# метод keys() – возвращает список ключей словаря;
# метод values() – возвращает список значений словаря.


#           *************       Добавление и изменение элементов в словаре      *********

# Чтобы изменить значение по определенному ключу в словаре, достаточно использовать индексацию вместе с оператором присваивания.
# При этом если ключ уже присутствует в словаре, его значение заменяется новым, если же ключ отсутствует, то в словарь будет добавлен новый элемент

# info = {'name': 'Sam',
#         'age': 28,
#         'job': 'Teacher'}
#
# info['name'] = 'Timur'                    # изменяем значение по ключу name
# info['email'] = 'timyr-guev@yandex.ru'    # добавляем в словарь элемент с ключом email
#
# print(info)


# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     if num not in result:
#         result[num] = 1
#     else:
#         result[num] += 1

# Этот код можно улучшить с помощью метода get().

#                                   ***********  Метод get()    ***********************

# Для того, чтобы избежать возникновения ошибки в случае отсутствия ключа в словаре можно использовать метод get(),
# способный кроме ключа принимать и второй аргумент — значение, которое вернется, если заданного ключа нет.
# Когда второй аргумент не указан, то метод в случае отсутствия ключа возвращает None.

# info = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# item1 = info.get('salary')
# item2 = info.get('salary', 'Информации о зарплате нет')
#
# print(item1)
# print(item2)

# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     result[num] = result.get(num, 0) + 1
#
# print(result)



#                  *************** Метод update()   ****************

# Метод update() – реализует своеобразную операцию конкатенации для словарей. Он объединяет ключи и значения одного
# словаря с ключами и значениями другого. При совпадении ключей в итоге сохранится значение словаря, указанного в качестве аргумента метода update()

# info1 = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# info2 = {'age': 30,
#         'city': 'New York',
#         'email': 'bob@web.com'}
#
# info1.update(info2)
#
# print(info1)

# В Python 3.9 появились операторы | и |= которые реализуют операцию конкатенации словарей.

# info1 = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# info2 = {'age': 30,
#         'city': 'New York',
#         'email': 'bob@web.com'}
#
# info1 |= info2
#
# print(info1)


#               *******************     Метод setdefault()      ************
# Метод setdefault() позволяет получить значение из словаря по заданному ключу, автоматически добавляя элемент словаря, если он отсутствует.
# Метод принимает два аргумента:
#
#  key: ключ, значение по которому следует получить, если таковое имеется в словаре, либо создать.
#  default: значение, которое будет использовано при добавлении нового элемента в словарь.

# Сценарий 1. Если ключ key присутствует в словаре, то метод возвращает значение по заданному ключу (независимо от того, передан параметр default или нет).
# info = {'name': 'Bob',
#         'age': 25}
#
# name1 = info.setdefault('name')           # параметр default не задан
# name2 = info.setdefault('name', 'Max')    # параметр default задан
#
# print(name1)
# print(name2)


# Сценарий 2. Если ключ key отсутствует в словаре, то метод вставляет переданное значение default по заданному ключу.
# info = {'name': 'Bob',
#         'age': 25}
#
# job = info.setdefault('job', 'Dev')
# print(info)
# print(job)


# info = {'name': 'Bob',
#         'age': 25}
#
# job = info.setdefault('job')
# print(info)
# print(job)

#       ****************************        Удаление элементов из словаря       ******************

# Существует несколько способов удаления элементов из словаря:
#
# оператор del;
# метод pop();
# метод popitem();
# метод clear().


#           ***************         Оператор del            ****

# С помощью оператора del можно удалять элементы словаря по определенному ключу.
# info = {'name': 'Sam',
#         'age': 28,
#         'job': 'Teacher',
#         'email': 'timyr-guev@yandex.ru'}
#
# del info['email']    # удаляем элемент имеющий ключ email
# del info['job']      # удаляем элемент имеющий ключ job
#
# print(info)

#  Если удаляемого ключа в словаре нет, возникнет ошибка KeyError


#               *********   Метод pop() ****************

# Оператор del удаляет из словаря элемент по заданному ключу вместе с его значением. Если требуется получить само значение удаляемого элемента, то нужен метод pop().

# info = {'name': 'Sam',
#         'age': 28,
#         'job': 'Teacher',
#         'email': 'timyr-guev@yandex.ru'}
#
# email = info.pop('email')          # удаляем элемент по ключу email, возвращая его значение
# job = info.pop('job')              # удаляем элемент по ключу job, возвращая его значение
#
# print(email)
# print(job)
# print(info)


# Единственное отличие этого способа удаления от оператора del — он возвращает удаленное значение.
# В остальном этот способ идентичен оператору del. В частности, если удаляемого ключа в словаре нет, возникнет ошибка KeyError.

# Чтобы ошибка не появлялась, этому методу можно передать второй аргумент. Он будет возвращен, если указанного ключа в словаре нет.
# Это позволяет реализовать безопасное удаление элемента из словаря:

# surname = info.pop('surname', None)

#           ********************        Метод popitem()     *************

# Метод popitem() удаляет из словаря последний добавленный элемент и возвращает удаляемый элемент в виде кортежа (ключ, значение)

# info = {'name': 'Bob',
#      'age': 25,
#      'job': 'Dev'}
#
# info['surname'] = 'Sinclar'
#
# item = info.popitem()
#
# print(item)
# print(info)


#           *********************       Метод clear()       **************

# Метод clear() удаляет все элементы из словаря.

# info = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# info.clear()
#
# print(info)


#           ***********************     Метод copy()            ********

# info = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# info_copy = info.copy()
#
# print(info_copy)
# Не стоит путать копирование словаря (метод copy()) и присвоение новой переменной ссылки на старый словарь.

# info = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# new_info = info
# new_info['name'] = 'Tim'
#
# print(info)

# Таким образом, когда мы изменяем словарь new_info, меняется и словарь info. Если необходимо изменить один словарь, не изменяя второй, используют метод copy().

# info = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# new_info = info.copy()
# new_info['name'] = 'Tim'
#
# print(info)
# print(new_info)


# Примечание 1. Словарь можно использовать вместо нескольких вложенных условий, если вам нужно проверить число на равенство.
# Например вместо
# num = int(input())
#
# if num == 1:
#     description = 'One'
# elif num == 2:
#     description = 'Two'
# elif num == 3:
#     description = 'Three'
# else:
#     description = 'Unknown'
#
# print(description)
#
# # можно написать
# num = int(input())
#
# description = {1: 'One', 2: 'Two', 3: 'Three'}
#
# print(description.get(num, 'Unknown'))


# result = {}
#
# for i in range(1, 16):
#     result.setdefault(i, i ** 2)
#
# print(result)

# **********************

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# result = {}
#
# for key in dict1:
#     if key in dict2:
#         result.setdefault(key, dict1.get(key) + dict2.get(key))
#     else:
#         result.setdefault(key, dict1.get(key))
#
# print(result)
#
# result.update(dict2)
# print(result)

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# result = {}
#
# for key in dict1:
#     if key in dict2:
#         result.setdefault(key, (dict1.get(key) + dict2.get(key)))
#     else:
#         result.setdefault(key, dict1.get(key))
#
#
# for key in dict2:
#     if key not in result:
#         result.setdefault(key, dict2.get(key))

# ************* (ОТ ПОЛЬЗОВАТЕЛЯ)

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# result = dict1.copy()
# for key, value in dict2.items():
#     result[key] = result.get(key, 0) + value


# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
#
# result = {}
#
#
# for el in text:
#     result[el] = result.setdefault(el, 0) + 1

# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange' \
#     ' barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot' \
#     ' currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate' \
#     ' barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot' \
#     ' currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant' \
#     ' orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
#
# s = s.split()
# res = {}
#
# for el in s:
#     res[el] = res.get(el, 0) + 1
#
# copy_res = res.copy()
#
# for key, value in res.items():
#     if res[key] >= max(res.values()):
#         continue
#     else:
#         del copy_res[key]
#
# print(min(copy_res))



# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
#
# for el in pets:
#     result.setdefault(el[1:], []).append(el[0])


# САМОЕ РЕДКОЕ СЛОВО

# words = [el.strip('.,!?:;-') for el in input().lower().split()]
#
# my_dict = {}
#
# for el in words:
#     my_dict[el] = my_dict.get(el, 0) + 1
#
# min_value = min(my_dict.values())
# my_list = []
# for key, value in my_dict.items():
#     if value == min_value:
#         my_list.append(key)
#
# print(min(my_list))


# САМОЕ РЕДКОЕ СЛОВО (ОТ ПОЛЬЗОВАТЕЛЯ)(ЧЕРЕЗ ЛЯМБДА ФУНКЦИЮ)

# st = [i.strip('.,!?:;-') for i in input().lower().split()]
#
# print(min(st, key=lambda x: (st.count(x), x)))


# ИСПРАВЛЕНИЕ ДУБЛИКАТОВ

# letters = input().split()
#
# my_dict = {}
#
# for el in letters:
#     my_dict[el] = my_dict.get(el, 0) + 1
#     if my_dict[el] == 1:
#         print(el, end=' ')
#     else:
#         print(el + '_' + str(my_dict[el] - 1), end=' ')


# ИСПРАВЛЕНИЕ ДУБЛИКАТОВ (ОТ ПОЛЬЗОВАТЕЛЯ)
# lst = input().split()
# res = {}
# for c in lst:
#     if c in res:
#         print(f'{c}_{res[c]}', end=' ')
#     else:
#         print(c, end=' ')
#     res[c] = res.get(c, 0) + 1


# ИСПРАВЛЕНИЕ ДУБЛИКАТОВ (ОТ ПОЛЬЗОВАТЕЛЯ)
# d, res = {}, []
# for w in input().split():
#     n = d[w] = d.get(w, -1) + 1
#     res.append(f'{w}_{n}' if n > 0 else w)
# print(*res)

# СТРАНЫ И ГОРОДА

# my_list = []
#
# for el in range(int(input())):
#     my_list.append(input().split())
#
# my_dict = {}
#
# for el in my_list:
#     my_dict[tuple(el[1:])] = el[0]
#
# for _ in range(int(input())):
#     x = input()
#     for key, value in my_dict.items():
#         if x in key:
#             print(my_dict[key])


# СТРАНЫ И ГОРОДА (ОТ ПОЛЬЗОВАТЕЛЯ) (БЕЗ КОРТЕЖА)

# d = {}
# for _ in range(int(input())):
#     country, *cities = input().split()
#     d.update(dict.fromkeys(cities, country))
# for _ in range(int(input())):
#     print(d[input()])

# СТРАНЫ И ГОРОДА (ОТ ПОЛЬЗОВАТЕЛЯ) (ПРОВЕРКА В ЗНАЧЕНИИ И ВЫВОД КЛЮЧА)
# d = {}
# for i in range(int(input())):
#     l = input().split()
#     d[l[0]] = l[1:]
#
# for i in range(int(input())):
#     k = input()
#     for key, value in d.items():
#         if k in value:
#              print(key)



