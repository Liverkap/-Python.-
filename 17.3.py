#                                       работа с текстовыми файлами

#                                       Позиция в файле

# Вызов методов read(), readlines(), readline() перемещает текущую позицию туда, где завершилось чтение.
# Для методов read() и readlines() это конец файла, для метода readline() – следующая строка после прочитанной.

# Текущую позицию обычно называют "курсор"

# Если мы считаем две строки с помощью метода readline()
# file = open('languages.txt', 'r', encoding='utf-8')
# line1 = file.readline()
# line2 = file.readline()
#
# file.close()

# Чтение всегда происходит слева направо от курсора. Таким образом, если после двух вызовов метода readline() вызвать метод read(), он считает не весь файл, а только оставшиеся строки:
# file = open('languages.txt', 'r', encoding='utf-8')
# line1 = file.readline()
# line2 = file.readline()
# remaining_lines = file.read()    # считывание начинается с 3 строки до конца файла
#
# file.close()

# После того, как мы считали все строки файла, курсор находится в конце

# Для повторного чтения данных из файла, можно:
# переоткрыть файл, тогда курсор снова попадёт в начало;
# переместить курсор с помощью файлового метода seek()



#           ***********************             Файловый метод seek()       ******

# айловый метод seek() задаёт позицию курсора в байтах от начала файла. Чтобы перевести курсор в самое начало файла
# необходимо вызвать метод seek(), передав ему в качестве аргумента значение 0.

# file = open('languages.txt', 'r', encoding='utf-8')
# line1 = file.readline()
# file.seek(0)               # переводим курсор в самое начало
# line2 = file.readline()
#
# print(line1, line2)
#
# file.close()

# Метод seek() не очень полезен при работе с текстовыми файлами, так как не учитывает разделение текста на строки. А вот при работе с файлами в двоичном режиме умение работать с позицией и смещениями очень важно!
# Будьте аккуратны с символами, использующими более 1 байта (кириллица в кодировке utf-8), обращение к "промежуточному" байту может вызвать ошибку.



# Если метод seek() устанавливает курсор (текущую позицию), то метод tell() получает ее

# file = open('languages.txt', 'r', encoding='utf-8')
# print(file.tell())
# line1 = file.readline()
# print(file.tell())
#
# file.close()

# В самом начале курсор (текущая позиция) равен нулю, после считывания первой строки, курсор смещается на 8 байт (по байту на каждый из символов 'P', 'y', 't', 'h', 'o', 'n' и два байта на символ перевода строки '\n')


#        ***********************             Менеджер контекста      ******
# Как уже сказано, важно своевременно закрывать файлы с помощью метода close(). Закрытие файлов вручную, а также
# отдача закрытия на откуп среде исполнения, обладают существенным недостатком: если между открытием файла и его
# закрытием произойдёт ошибка, в лучшем случае файл окажется открыт слишком долго, а в худшем случае часть данных не сохранится.
#
# Хочется иметь возможность автоматически закрывать файл сразу после окончания работы с ним и осуществлять закрытие даже
# при возникновении ошибки. Файловые объекты уже умеют работать в таком режиме, но для этого их нужно использовать как менеджеры контекста.
#
# Менеджер контекста — объект, реализующий одноименный протокол. Объекты, реализующие этот протокол, позволяют использовать следующий специальный синтаксис

# with object as name:
    # Здесь нам доступен ресурс name.
    # Это тело with-блока.
# А здесь ресурс name уже освобождён, даже если в теле with-блока произошла ошибка.

# Весь код в теле with-блока работает "в контексте". Чаще всего контекст подразумевает выделение некоего ресурса, например, файла.
# По выходу из контекста ресурс автоматически освобождается, даже если при выполнении блока возникло исключение.

# Как только закончится код, оформленный с отступами в with (аналогичные отступы в циклах или функциях), это будет означать, что контекст закончился, и Python автоматически закроет файл.

# Приведенный ниже код:
# file = open('languages.txt', 'r', encoding='utf-8')
#
# for line in file:
#     print(line)
#
# file.close()              # ручное закрытие файла
#
# print('Файл закрыт')
#
# # можно переписать в виде
# with open('languages.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line)
#                           # автоматическое закрытие файла
# print('Файл закрыт')

# С помощью менеджера контекста можно работать с несколькими файлами.
# with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
#     # обработка файлов

# with open('input.txt', encoding='utf-8') as file:
#     print('Repeat after me:', file.readline().strip())
#     for line in file:
#         print(line.strip() + '!')


# text = '''pop
# goes
# the
# weasel!'''
#
# with open('input.txt', 'w') as f:
#     f.write(text)
#
# with open('input.txt', encoding='utf-8') as file:
#     print('Repeat after me:', file.readline().strip())
#     for line in file:
#         print(line.strip() + '!')


# ПЕРЕВОРОТ СТРОКИ

# with open('text.txt', encoding='utf=8') as file:
#     for line in file:
#         print(line[::-1])

# ОБРАТНЫЙ ПОРЯДОК

# with open('data.txt', encoding='utf-8') as file:
#     content = file.readlines()
#     for el in reversed(content):
#         print(el.rstrip())
#
# # ОБРАТНЫЙ ПОРЯДОК(ОТ ПОЛЬЗОВАТЕЛЯ)
# with open('data.txt', encoding='utf-8') as file:
#     print(*file.readlines()[::-1], sep='')

# ОБРАТНЫЙ ПОРЯДОК(ОТ ПОЛЬЗОВАТЕЛЯ)
# with open('data.txt', encoding='UTF-8') as file:
#     for i in file.readlines()[::-1]:
#         print(i.strip())


# ДЛИННЫЕ СТРОКИ

# with open('lines.txt', encoding='utf-8') as file:
#     content = [el.rstrip() for el in file.readlines()]
#     max_len = 0
#     for el in content:
#         if max_len < len(el):
#             max_len = len(el)
#
#     print(*list(filter(lambda x: len(x) == max_len, content)), sep='\n')
#
# # ДЛИННЫЕ СТРОКИ(ОТ ПОЛЬЗОВАТЕЛЯ)
# with open('lines.txt') as f:
#     max_len, longest = 0, []
#     for line in f:
#         line = line.rstrip('\n')
#         line_len = len(line)
#         if line_len == max_len:
#             longest.append(line)
#         elif line_len > max_len:
#             max_len, longest = line_len, [line]
#
# print('\n'.join(longest))
#
# # ДЛИННЫЕ СТРОКИ(ОТ ПОЛЬЗОВАТЕЛЯ)
# with open('lines.txt') as f:
#     lines = [line.strip() for line in f.readlines()]
#     longest = max(map(len, lines))
#     print(*filter(lambda x: len(x) == longest, lines), sep='\n')
#
# # ДЛИННЫЕ СТРОКИ(ОТ ПОЛЬЗОВАТЕЛЯ)
# with open('lines.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#     for line in lines:
#         if len(line) == len(max(lines, key=len)):
#             print(line.strip())


# СУММА ЧИСЛ В СТРОКАХ

# with open('numbers.txt', encoding='utf-8') as f:
#     content = [el.split() for el in f.readlines()]
#     new_list = []
#     for el in content:
#         res = 0
#         for i in range(len(el)):
#             res += int(el[i])
#         new_list.append(res)
#
#     print(*new_list, sep='\n')
#
# # СУММА ЧИСЛ В СТРОКАХ(ОТ ПОЛЬЗОВАТЕЛЯ)
# with open('numbers.txt') as f:
#     for line in f:
#         print(sum(map(int, line.split())))
#
# # СУММА ЧИСЛ В СТРОКАХ(ОТ ПОЛЬЗОВАТЕЛЯ)
# with open('numbers.txt') as f:
#     print(*(sum(map(int, line.split())) for line in f), sep='\n')
#
# # СУММА ЧИСЛ В СТРОКАХ(ОТ ПОЛЬЗОВАТЕЛЯ)
# with open('numbers.txt', encoding='utf-8') as file:
#     f = map(lambda x: x.split(), file.readlines())
#     print(*map(lambda x: sum(map(lambda i: int(i), x)), f), sep='\n')


# СУММА ЧИСЕЛ В ФАЙЛЕ

with open('nums.txt', encoding='utf-8') as f:
    content = [el.split() for el in f.readlines()]
    # content = f.readlines()
    #
    print(content)















