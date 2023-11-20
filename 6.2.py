# Функция tuple()

# Встроенная функция list() может применяться для преобразования кортежа в список

# number_tuple = (1, 2, 3, 4, 5)
# number_list = list(number_tuple)
# print(number_list)
#
# Встроенная функция tuple()  может применяться для преобразования списка в кортеж.
# str_list = ['один', 'два', 'три']
# str_tuple = tuple(str_list)
# print(str_tuple)

#
# text = 'hello python'
# str_tuple = tuple(text)
# print(str_tuple)


# когда надо изменить один символ строки
# s = 'симпотичный'
# print(s)
# a = list(s)
# a[4] = 'а'
# s = ''.join(a)
# print(s)
#
# # когда надо изменить символ Кортежа
# writer = ('Лев Толстой', 1827)
# print(writer)
# a = list(writer)
# a[1] = 1828
# writer = tuple(a)
# print(writer)


# Операция конкатенации + и умножения на число *
#
# print((1, 2, 3, 4) + (5, 6, 7, 8))
# print((7, 8) * 3)
# print((0,) * 10)


# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print('Сумма всех элементов кортежа =', sum(numbers))
#
#
# numbers = (3, 4, 10, 3333, 12, -7, -5, 4)
# print('Минимальный элемент кортежа =', min(numbers))
# print('Максимальный элемент кортежа =', max(numbers))


# numbers = (3, 4, 10, 3333, 12, -7, -5, 4)
# print('Минимальный элемент кортежа =', min(numbers))
# print('Максимальный элемент кортежа =', max(numbers))
#
#
# names = ('Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur')
# cnt1 = names.count('Timur')
# cnt2 = names.count('Gvido')
# cnt3 = names.count('Josef')
#
# print(cnt1)
# print(cnt2)
# print(cnt3)


# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[3:][:-2])


# countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
# number = len(countries)
# print(number)

# numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
#
# print(min(numbers) + max(numbers))

# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
# index = countries.index('Slovenia')
# print(index)


# numbers1 = (1, 2, 3)
# numbers2 = (6,)
# numbers3 = (7, 8, 9, 10, 11, 12, 13)
#
# print(numbers1 * 2 + numbers2 * 9 + numbers3)

# city_name = input()
# city_year = int(input())
# city = (city_name, city_year)
# print(city)


# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# non_empty_tuples = [el for el in tuples if len(el) > 0]
#
# print(non_empty_tuples)


tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = [el[:-1] + (100, ) for el in tuples]
print(new_tuples)