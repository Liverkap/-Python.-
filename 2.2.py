# КООРДИНАТНЫЕ ЧЕТВЕРТИ

# n = int(input())
#
# my_list = []
#
# for _ in range(n):
#     my_list.append(input().split())
#
# count_1 = 0
# count_2 = 0
# count_3 = 0
# count_4 = 0
#
# for c in my_list:
#     if int(c[0]) > 0 and int(c[1]) > 0:
#         count_1 += 1
#     elif int(c[0]) < 0 and int(c[1]) > 0:
#         count_2 += 1
#     elif int(c[0]) < 0 and int(c[1]) < 0:
#         count_3 += 1
#     elif int(c[0]) > 0 and int(c[1]) < 0:
#         count_4 += 1
#
# print(f'Первая четверть: {count_1}')
# print(f'Вторая четверть: {count_2}')
# print(f'Третья четверть: {count_3}')
# print(f'Четвертая четверть: {count_4}')


# КООРДИНАТНЫЕ ЧЕТВЕРТИ (ОТ ПРЕПОДАВАТЕЛЯ)

n = int(input())

count = [0] * 4
names = ['Первая четверть:', 'Вторая четверть:', 'Третья четверть:', 'Четвертая четверть:']

for _ in range(n):
    x, y = [int(num) for num in input().split()]
    if x > 0 and y > 0:
        count[0] += 1
    elif x < 0 and y > 0:
        count[1] += 1
    elif x < 0 and y < 0:
        count[2] += 1
    elif x > 0 and y < 0:
        count[3] += 1

for i in range(4):
    print(names[i], count[i])












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
#     elif name1 == 'камень' and name2 != 'бумага' or name1 == 'ножницы' and name2 != 'камень' or name1 == 'бумага' and name2 != 'ножницы' :
#         return 'Тимур'
#     else:
#         return 'Руслан'
#
# timur = input()
# ruslan = input()
#
# print(chek_res(timur, ruslan))

# # КАМЕНЬ, НОЖНИЦЫ, БУМАГА (ОТ ПРЕПОДАВАТЕЛЯ)
# options = ["камень", "ножницы", "бумага"]
# results = ["ничья", "Руслан", "Тимур"]
#
# timur_move = input()
# ruslan_move = input()
#
# case = options.index(timur_move) - options.index(ruslan_move)
# res = results[case]
#
# print(res)

# КАМЕНЬ, НОЖНИЦЫ, БУМАГА (ОТ ПОЛЬЗОВАТЕЛЯ)
# a, b = input(), input()
# print('ничья' if a == b else 'Тимур' if a + b in ('каменьножницы', 'бумагакамень', 'ножницыбумага') else 'Руслан')


# КАМЕНЬ, НОЖНИЦЫ, БУМАГА, ЯЩЕРИЦА, СПОК

# timur, ruslan = input(), input()
#
# my_list = ['каменьножницы', 'бумагакамень', ' ножницыбумага', 'Споккамень',
#            'ножницыящерица', 'ящерицабумага', 'ящерицаСпок', 'каменьящерица']
#
# if timur == ruslan:
#     print('ничья')
# elif timur + ruslan in my_list:
#     print('Тимур')
# else:
#     print('Руслан')


# КАМЕНЬ, НОЖНИЦЫ, БУМАГА, ЯЩЕРИЦА, СПОК (ВАРИАНТ ЧЕРЕЗ ИНДЕКСЫ)

# options = ["камень", "ящерица", "Спок", "ножницы", "бумага" ] # расставляем в том порядке, что каждый текущий бьёт следующего
# results = ["ничья", "Руслан", "Тимур", "Руслан", "Тимур"]
#
# timur, ruslan = input(), input()
# case = options.index(timur) - options.index(ruslan)
#
# res = results[case]
# print(res)

# ОРЕЛ И РЕШКА

# string = input().split('О')
#
# print(len(max(string)))

# КРЕМНИЕВАЯ ДОЛИНА

# n = int(input())
#
# my_list = []
#
# for _ in range(n):
#     my_list.append(input())
#
# virus = 'anton'
# v = []
#
# for i in range(len(my_list)):
#     check_list = []
#     holod = []
#     for j in range(len(my_list[i])):
#         #holod = []
#         if my_list[i][j] in virus:
#             holod += my_list[i][j]
#     #print(holod)
#     if ''.join(holod) == virus:
#         ''.join(holod)
#         v.append(my_list.index(my_list[i]) + 1)
# print(*v)



# РОСКОМНАДЗОР ЗАПРЕТИЛ БУКВУ А

# string = input() + ' ' + 'запретил букву'
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#
# print(string)



