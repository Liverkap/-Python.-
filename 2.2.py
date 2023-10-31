








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
# # РАЗЛИЧНЫЕ ЭЛЕМЕНТЫ (ОТ ПРЕПОДАВАТЕЛЯ)
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

