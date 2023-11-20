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

x = ('Тургенев', 14)
y = ('Есенин', 13)
print(x > y)