# def func(name, age=20):
#     print(name, age)
#
# func('Emma', 25)

# def display(**kwargs):
#     for i in kwargs:
#         print(i, end=' ')
#
# display(emp='Kelly', salary=9000)

# num = int('1000001', 2)
# print(num)



# ПИСЬМО ДЛЯ ЭКЗАМЕНА
# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
#     letter = f'To: {mail}\n' \
#              f'Приветствую, {name}!\n' \
#              f'Вам назначен экзамен, который пройдет {date}, в {time}.\n' \
#              f'По адресу: {place}.\n' \
#              f'Экзамен будет проводить {teacher} в кабинете {number}.\n' \
#              f'Желаем удачи на экзамене!'
#
#     return letter
#
#
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
# print()
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00',
#                       'Часова 23, корпус 2', 'Василь Ярошевич', 23))


# PRETTY PRINT
# ***********
# def pretty_print(data, side='-', delimiter='|'):
#     numbers = []
#     for i in range(len(data)):
#         s = delimiter + ' ' + str(data[i])
#         numbers.append(s)
#
#     b = []
#     c = ' '.join(numbers) + ' ' + delimiter
#     x = ' ' + side * (len(c) - 2) + ' '
#
#     b.append(x)
#     b.append(c)
#     b.append(x)
#     print(*b, sep='\n')




# ***********(ДЯЛ ТЕСТОВ)
def pretty_print(data, side='-', delimiter='|'):
    numbers = []
    for i in range(len(data)):
        s = delimiter + ' ' + str(data[i])
        print(s)
        numbers.append(s)
    print(numbers)

    b = []
    c = ' '.join(numbers) + ' ' + delimiter
    x = ' ' + side * (len(c) - 2) + ' '

    b.append(x)
    b.append(c)
    b.append(x)
    print(b)
    # print(*b, sep='\n')
# **********

pretty_print([1, 2, 10, 23, 123, 3000])