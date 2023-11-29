# Основы работы с множествами

#               ****************        Функция len()       ***************

# myset1 = {2, 2, 4, 6, 6}
# myset2 = set([1, 2, 2, 3, 3, 4, 4, 5, 5])
# myset3 = set('aaaaabbbbccccddd')
#
# print(len(myset1))
# print(len(myset2))
# print(len(myset3))

#           ********************        Оператор принадлежности in  **********

# numbers = {2, 4, 6, 8, 10}
#
# if 2 in numbers:
#     print('Множество numbers содержит число 2')
# else:
#     print('Множество numbers не содержит число 2')
#
# # Оператор принадлежности in работает очень быстро на множествах, намного быстрее чем на списках.
# # Поэтому если требуется часто осуществлять поиск в коллекции уникальных данных, то множество – подходящий выбор.
#
#
#
# #               **************      Встроенные функции sum(), min(), max()      *************
#
# numbers = {2, 2, 4, 6, 6}
# print('Сумма всех элементов множества =', sum(numbers))


# print(len(set(input())))

# numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
#
# print(min(numbers) + max(numbers))
# print(sum((min(numbers), max(numbers))))
# print(sum([min(numbers), max(numbers)]))

# numbers = {20, 6, 8, 18, 18, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 12, 8, 8, 10, 4, 2, 2, 2, 16, 20}
# average = sum(numbers) / len(numbers)
#
# print(average)


#           ******************* Перебор элементов множества *****************

# numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
#
# for num in numbers:
#     print(num)

# Мы также можем использовать операцию распаковки множества.

# numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
#
# print(*numbers, sep='\n')

# Если нужно гарантировать порядок вывода элементов (по возрастанию / убыванию), то необходимо воспользоваться встроенной функцией sorted()


# numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
#
# sorted_numbers = sorted(numbers)
# print(*sorted_numbers, sep='\n')

# Встроенная функция sorted() имеет опциональный параметр reverse. Если установить этот параметр в значение True, произойдет сортировка по убыванию
# numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
#
# sortnumbers = sorted(numbers, reverse=True)
# print(type(sortnumbers))
# print(*sortnumbers, sep='\n')



#               *********************   Сравнение множеств  ************

# myset1 = {1, 2, 3, 3, 3, 3}
# myset2 = {2, 1, 3}
# myset3 = {1, 2, 3, 4}
#
# print(myset1 == myset2)
# print(myset1 == myset3)
# print(myset1 != myset3)


# myset1 = set([1, 2, 3, 4, 5])
# myset2 = set('12345')
#
# print(myset1)
# print(myset2)
#
# print(myset1 == myset2)


# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
#
# total = 0
#
# for el in numbers:
#     total += el ** 2
#
# print(total)

# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
#
# # my_list = [el for el in fruits]
# print(*sorted(fruits, reverse=True), sep='\n')
#
# # (ОТ ПОЛЬЗОВАТЕЛЯ)
#
# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
#
# [print(i) for i in sorted(fruits, reverse = True)]


# Количество различных символов

# print(len(set(input())))


# Неповторимые цифры

# s = str(input())
#
# for i in range(len(s)):
#     x = s.count(s[i])
#     if x > 1:
#         print('NO')
#         break
# else:
#     print('YES')


# Неповторимые цифры (С ПОМОЩЬЮ МНОЖЕСТВ)

# s = input()
#
# if len(s) == len(set(s)):
#     print('YES')
# else:
#     print('NO')