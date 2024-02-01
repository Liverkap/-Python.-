#           ******************* ВЛОЖЕННЫЕ СПИСКИ    *****************



# my_list = [[0], [1, 2], [3, 4, 5]]
#
# print(my_list)
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(len(my_list))


# my_list = ['Python', [10, 20, 30], ['Beegeek', 'Stepik!']]
#
# print(my_list[0][2])       # индексирование строки 'Python'
# print(my_list[1][1])       # индексирование списка [10, 20, 30]
# print(my_list[2][-1])      # индексирование списка ['Beegeek', 'Stepik!']
# print(my_list[2][-1][-1])  # индексирование строки 'Stepik!'


#           **********      Функции len(), max(), min()     ***********************

# total = 0
# my_list = [[0], [1, 2], [3, 4, 5], [], [10, 20, 30]]
#
# for li in my_list:
#     total += len(li)
#
# print(total)


# list1 = [1, 7, 12, 0, 9, 100]
# list2 = [1, 7, 90]
# list3 = [1, 10]
#
# print(min(list1, list2, list3))
# print(max(list1, list2, list3))


# list1 = [[1, 7, 12, 0, 9, 100], [1, 7, 90], [1, 10]]
# list2 = [['a', 'b'], ['a'], ['d', 'p', 'q']]
#
# print(min(list1))
# print(max(list1))
# print(min(list2))
# print(max(list2))


# list1 = [[0, [9, 2]], [1, [4, 6, 3], [5, 2, 3], 8, 3]]
#
# print(list1[1][2][1])


# ПОПОЛНЕНИЕ ПОДСПИСКА
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#
# list1[2][2].append(7000) #пополнение подсписка
#
# print(list1)

# РАСШИРЕНИЕ ПОДСПИСКА
# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# sub_list = ['h', 'i', 'j']
#
# list1[2][1][2].extend(sub_list) # расширение подсписка
# print(list1)


# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
#
# for el in list1:
#     for i in range(len(el)):
#         if el[i] > maximum:
#             maximum = el[i]
#
# print(maximum)

# (ОТ ПРЕПОДАВАТЕЛЯ)
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
#
# for li in list1:
#     if max(li) > maximum:
#         maximum = max(li)
# print(maximum)


#
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
#
# for i in range(len(list1)):
#     list1[i].reverse()
#
# print(list1)


# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
#
# for el in list1:
#     for i in range(len(el)):
#         total += el[i]
#         counter += 1
#
# res = total / counter
#
# print(res)


# (ОТ ПРЕПОДАВАТЕЛЯ)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
#
# for li in list1:
#     total += sum(li)
#     counter += len(li)
#
# print(total / counter)



