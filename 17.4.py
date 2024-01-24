                                    # работа с текстовыми файлами
# Урок посвящен работе с файлами. Мы изучим методы записи в файл write() и writelines()

#                                   Запись данных в файлы
# Для записи используются два файловых метода:
# write() – записывает переданную строку в файл;
# writelines() – записывает переданный список строк в файл


#               *****************       Метод write()       ****
# Общий формат применения файлового метода write()
# файловая_переменная.writе(строковое_значение)

# файловая переменная – это имя переменной, которая ссылается на файловый объект;
# строковое значение – это символьная последовательность, которая будет записана в файл
#
# Для записи данных в файл он должен быть открыт для записи (режимы 'w', 'а', 'r+'), иначе произойдет ошибка


# with open('myfile.txt', 'w', encoding='utf-8') as file:
#     file.write('Python and beegeek forever\n')
#     file.write('We love stepik <3')
#
# # Если файл открыт в режиме 'a', то запись происходит в самый конец файла
#
# with open('myfile.txt', 'a', encoding='utf-8') as file:
#     file.write('Python and beegeek forever\n')
#     file.write('We love stepik <3')

# Если файл открыт в режиме 'r+', то происходит частичная перезапись его содержимого
# with open('myfile.txt', 'r+', encoding='utf-8') as file:
#     file.write('Python and beegeek forever\n')
#     file.write('We love stepik.')


#           ****************        Метод writelines()  *************
# Последовательные вызовы метода write() дописывают текст в конец файла.
#
# Приведенный ниже код создает файл philosophers.txt и записывает в него три строки текста:
# with open('philosophers.txt', 'w', encoding='utf-8') as file:
#     file.write('Джoн Локк\n')
#     file.write('Дэвид Хьюм\n')
#     file.write('Эдмyнд Берк\n')


# На практике часто приходится записывать в файл содержимое целого списка. Это можно сделать с помощью цикла или метода writelines(), что удобнее.
# Метод writelines() принимает в качестве аргумента список строк и записывает его в файл

# philosophers = ['Джoн Локк\n', 'Дэвид Хьюм\n', 'Эдмyнд Берк\n']
#
# with open('philosophers.txt', 'w', encoding='utf-8') as file:
#     file.writelines(philosophers)

# Обратите внимание, что все записанные в файл строковые значения оканчиваются символом '\n', экранированной
# последовательностью новой строки. Символ '\n' не только отделяет находящиеся в файле значения друг от друга,
# но и обеспечивает появление каждого из них на отдельной строке во время просмотра данных в текстовом редакторе

# Такой вариант записи предпочтителен, когда нужно записать большой объем текста, который вы получаете и обрабатываете строчка за строчкой.
# Можно предварительно накопить весь текст в одну большую строку, однако для этого может потребоваться большой объём памяти.
# Гораздо лучше записывать строчки по мере готовности и writelines для этого подходит идеально!


#               ******************          Запись в файл с помощью функции print()     **********
# Для записи данных в файл можно также использовать встроенную функцию print().
# Для этого нужно передать ей еще один именованный аргумент file, указывающий на открытый файл. При этом функция print() автоматически добавляет переход на новую строку

# with open('philosophers_new.txt', 'w', encoding='utf-8') as output:
#     print('Джoн Локк', file=output)
#     print('Дэвид Хьюм', file=output)
#     print('Эдмyнд Берк', file=output)

# Мы можем использовать всю мощность встроенной функции print() для форматирования выводимого текста
# with open('philosophers_new_2.txt', 'w', encoding='utf-8') as output:
#     print('Джoн Локк', 'Дэвид Хьюм', 'Эдмyнд Берк', sep='***', file=output)

# Не забывайте, что файловые методы write() и writelines() не добавляют переход на новую строку, поэтому для перехода на новую строку в файле необходимо явно добавить символ '\n'

# И методы write() и writelines() пишут данные не в конец файла, а в текущую позицию, т.е. если переместиться с помощью метода seek() на какую-то другую позицию в файле, запись будет произведена в эту позицию

# Примечание 1. В некоторых операционных системах невыполнение операции закрытия файла может привести к потере данных.
# Данные сначала пишутся в буфер – небольшую область временного хранения в оперативной памяти. Когда буфер заполняется,
# система записывает его содержимое в файл. Это увеличивает производительность системы, потому что запись данных в
# оперативную память быстрее записи на диск. Процесс закрытия файла записывает любые несохраненные данные из буфера в файл.
# Чтобы принудительно записать содержимое буфера в файл, используется файловый метод flush().
#
# Примечание 2. Используйте конструкцию with для чтения и записи файлов. Закрывать файлы — полезная привычка, и если вы
# используете команду with при работе с файлами, вам не придется беспокоиться об их закрытии. Команда with автоматически закрывает файл за вас

#
# with open('words.txt', 'w') as file:
#     file.write('delphi+')
#     file.write('java')


# with open('names.txt', 'a') as file:
#     file.write('\n')
#     file.write('Michael\n')
#     file.write('Alexander')

# with open('words_2.txt', 'w') as output:
#     print('stepik', 'beegeek', 'iq-option', sep='*', end='+\n', file=output)
#     print('python', file=output)

