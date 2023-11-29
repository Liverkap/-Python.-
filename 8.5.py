#               ************  МЕТОДЫ МНОЖЕСТВ   ******************

#                                Метод add()

# numbers = {1, 1, 2, 3, 5, 8, 3}
#
# numbers.add('123')
# numbers.add(34)
#
# print(numbers)
#
# numbers = set()  # создаем пустое множество


# для использования метода add() требуется предварительно созданное множество, при этом оно может быть пустым.
# numbers.add(1)
# numbers.add(2)
# numbers.add(3)
# numbers.add(1)
#
# print(numbers)


#                   *************   Удаление элемента   ****************

# Для удаления элементов из множества используются методы:
#
#     remove()
#     discard()
#     pop()


#               Метод remove()
# Метод remove() — удаляет элемент из множества с генерацией исключения (ошибки) в случае, если такого элемента нет
#
# numbers = {1, 2, 3, 4, 5}
#
# numbers.remove(3)
# print(numbers)


#               Метод discard()

# Метод discard() — удаляет элемент из множества без генерации исключения (ошибки), если элемент отсутствует
# numbers = {1, 2, 3, 4, 5}
#
# numbers.discard(3)
# print(numbers)


#               Метод pop()
# Метод pop() — удаляет и возвращает случайный элемент из множества с генерацией исключения (ошибки) при попытке удаления из пустого множества.

# numbers = {1, 2, 3, 4, 5}
#
# print('до удаления:', numbers)
# num = numbers.pop()                 # удаляет случайный элемент множества, возвращая его
# print('удалённый элемент:', num)
# print('после удаления:', numbers)


#               Метод clear()

# numbers = {1, 2, 3, 4, 5}
# numbers.clear()
#
# print(numbers)



# *************************************

# myset = {'Yellow', 'Orange', 'Black'}
#
# myset.pop('Orange')
# print(myset)

# myset = set('python')
#
# item = myset.pop()
# print(item, len(myset))


# Уникальные символы 1

#
# myset = [input() for el in range(int(input()))]
#
# for el in myset:
#     print(len(set(el.lower())))

# Уникальные символы 1 (ОТ ПОЛЬЗОВАТЕЛЯ)
for _ in range(int(input())):
    print(len(set(input().lower())))