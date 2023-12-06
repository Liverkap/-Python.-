#                          ********     Подмножества и надмножества  ***

# Напомним, что множество set1 является подмножеством множества set2, если все элементы первого входят во второе.
# При этом множество set2 – надмножество множества set1.


#               ****************        Метод issubset()        **************

#  Данный метод возвращает значение True, если одно множество является подмножеством другого, и False, если не является.

# set1 = {2, 3}
# set2 = {1, 2, 3, 4, 5, 6}
#
# print(set1.issubset(set2))

# Для определения, является ли одно из множеств подмножеством другого, также применяются операторы <= (нестрогое подмножество) и < (строгое подмножество).
# set1 = {2, 3}
# set2 = {1, 2, 3, 4, 5, 6}
#
# print(set1 <= set2)

#           *********************   Метод issuperset()  **********

# Данный метод возвращает значение True, если одно множество является надмножеством другого, в противном случае он возвращает False

# set1 = {'a', 'b', 'c', 'd', 'e'}
# set2 = {'c', 'e'}
#
# print(set1.issuperset(set2))

# Для определения, является ли одно из множеств надмножеством другого, также применяются операторы >= (нестрогое надмножество) и > (строгое надмножество).


#               ******************      Метод isdisjoint()      **********

# Данный метод возвращает значение True, если множества не имеют общих элементов, и  False, когда множества имеют общие элементы.
#
# set1 = {1, 2, 3, 4, 5}
# set2 = {5, 6, 7}
# set3 = {7, 8, 9}
#
# print(set1.isdisjoint(set2))
# print(set1.isdisjoint(set3))
# print(set2.isdisjoint(set3))

#  Методы issuperset(), issubset(), isdisjoint() могут принимать в качестве аргумента не только множество (тип данных set),
#  но и любой итерируемый объект (список, строку, кортеж...). Сами же эти методы могут применяться только ко множеству (тип данных set)
#  или замороженному множеству (тип данных frozenset).

# Операторы >, <, >=, <= требуют наличия в качестве операндов множества.




# ОДИНАКОВЫЕ ЦИФРЫ

# myset1 = set(input())
# myset2 = set(input())
#
# if myset1.isdisjoint(myset2):
#     print('NO')
# else:
#     print('YES')

# ОДИНАКОВЫЕ ЦИФРЫ (ОТ ПОЛЬЗОВАТЕЛЯ) (ОТВЕТ ПО ИНДЕКСУ ИЗ КОРТЕЖА)

# print(('YES', 'NO')[set(input()).isdisjoint(set(input()))])


# ВСЕ ЦИФРЫ

# myset1 = set(input())
# myset2 = set(input())
#
# if myset1 >= myset2:
#     print('YES')
# else:
#     print('NO')


# myset1 = set(input())
# myset2 = set(input())
#
# print(('NO', 'YES')[myset1 >= myset2])

# УРОК ИНФОРМАТИКИ

# myset1 = set([int(el) for el in input().split()])
# myset2 = set([int(el) for el in input().split()])
# myset3 = set([int(el) for el in input().split()])
#
# f1_f2 = myset1.intersection(myset2)
# f3 = f1_f2.difference(myset3)
# print(*sorted(f3, reverse=True))


# УРОК ИНФОРМАТИКИ (ОТ ПРЕПОДАВАТЕЛЯ)

# set1 = set(int(i) for i in input().split())
# set2 = set(int(i) for i in input().split())
# set3 = set(int(i) for i in input().split())
#
# print(*sorted(set1 & set2 - set3, reverse=True))


# УРОК МАТЕМАТИКИ

# myset1 = set(int(el) for el in input().split())
# myset2 = set(int(el) for el in input().split())
# myset3 = set(int(el) for el in input().split())
#
# union1 = (myset1 | myset2 | myset3) - (myset1 & myset2 & myset3)
#
# print(*sorted(union1))

# УРОК ФИЗИКИ

# myset1 = set([int(el) for el in input().split()])
# myset2 = set([int(el) for el in input().split()])
# myset3 = set([int(el) for el in input().split()])
#
#
# dif1 = myset3.difference(myset2, myset1)
# print(*sorted(dif1, reverse=True))

# УРОК БИОЛОГИИ

myset1 = set([int(el) for el in input().split()])
myset2 = set([int(el) for el in input().split()])
myset3 = set([int(el) for el in input().split()])

marks = set(range(11))

dif = marks - myset1 - myset2 - myset3
print(*sorted(dif))

# УРОК БИОЛОГИИ (ОТ ПРЕПОДАВАТЕЛЯ)

set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())

print(*sorted(set(range(11)) - set1 - set2 - set3))

# УРОК БИОЛОГИИ (ОТ ПОЛЬЗОВАТЕЛЯ)
a, b, c = [{int(i) for i in input().split()} for _ in 'abc']
print(*sorted(set(range(11)) - (a | b | c)))

