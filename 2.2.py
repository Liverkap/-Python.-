








# БОЛЬШЕ ПРЕДЫДУЩЕГО
#
# seq = input().split()
#
# count = 0
#
# for i in range(len(seq) - 1):
#     current_digit = int(seq[i])
#     next_digit = int(seq[i + 1])
#     if current_digit < next_digit:
#         count += 1
#
# print(count)


# БОЛЬШЕ ПРЕДЫДУЩЕГО (ОТ ПРЕПОДАВАТЕЛЯ)

# numbers = [int(n) for n in input().split()]
# counter = 0
#
# for i in range(1, len(numbers)):
#     if numbers[i] > numbers[i - 1]:
#         counter += 1
#
# print(counter)


# НАЗАД, ВПЕРЕД И НАОБОРОТ

# numbers = [int(n) for n in input().split()]
#
# for i in range(1, len(numbers), 2):
#     numbers.insert(i-1, numbers.pop(i))
#
# print(*numbers)



# СДВИГ В РАЗВИТИИ

# numbers = [int(n) for n in input().split()]
#
# numbers.insert(0, numbers.pop(-1))
#
# print(*numbers)

# СДВИГ В РАЗВИТИИ (ОТ ПРЕПОДАВАТЕЛЯ)

# seq = input().split()
# new_seq = [seq[-1]] + seq[:-1]
#
# print(*new_seq)


# РАЗЛИЧНЫЕ ЭЛЕМЕНТЫ

# numbers = [int(i) for i in input().split()]
# count = 0
# my_list = []
#
# for c in numbers:
#     if c not in my_list:
#         my_list.append(c)
#         count += 1
#
# print(count)
#
#
# # РАЗЛИЧНЫЕ ЭЛЕМЕНТЫ (ОТ ПРЕПОДАВАТЕЛЯ)"
#
# numbers = input().split()
# counter = 1
#
# for i in range(len(numbers) - 1):
#     if numbers[i] != numbers[i + 1]:
#         counter += 1
#
# print(counter)
#
#
# # РАЗЛИЧНЫЕ ЭЛЕМЕНТЫ (ОТ ПОЛЬЗОВАТЕЛЯ)
#
# s=input().split()
# a=[]
# for i in s:
#     if i not in a:
#         a.append(i)
# print(len(a))


# ПРОИЗВЕДЕНИЕ ЧИСЕЛ

# n = int(input())
#
# numbers = [int(input()) for _ in range(n)]
# flag = False
# product_num = int(input())
#
# for i in range(1, n):
#     for j in range(i):
#         if numbers[i] * numbers[j] == product_num:
#             flag = True
#             break
#
# if flag is True:
#     print('ДА')
# else:
#     print('НЕТ')
#
#
# # ПРОИЗВЕДЕНИЕ ЧИСЕЛ (ОТ ПРЕПОДАВАТЕЛЯ)
#
# size = int(input())
# seq = [int(input()) for _ in range(size)]
# number = int(input())
# flag = False
#
# for i in range(size):
#     for j in range(size):
#         if i != j and seq[i] * seq[j] == number:
#             flag = True
#
# if flag:
#     print("ДА")
# else:
#     print("НЕТ")


# КАМЕНЬ, НОЖНИЦЫ, БУМАГА

# def chek_res(name1, name2):
#     if name1 == name2:
#         return 'ничья'
#     elif name1 == 'камень' and name2 == 'ножницы':
#         return 'Тимур'
#
# Timur = input()
# Ruslan = input()


# ОРЕЛ И РЕШКА

# string = input().split('О')
#
# print(len(max(string)))



# РОСКОМНАДЗОР ЗАПРЕТИЛ БУКВУ А

string = input() + ' ' + 'запретил букву'
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

print(string)



