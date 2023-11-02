#                   ******************* ТИП ДАННЫХ NoneType     ******************

# Концепция ключевого слова null заключается в том, что оно дает переменной нейтральное или "нулевое" поведение.
# В языке Python, слово null заменено на None, поскольку слово null звучит не очень дружелюбно, а None относится именно
# к требуемой функциональности – это ничего и не имеет поведения.


#           ********************* ЛИТЕРАЛ NONE  ***************************
#
# var = None
# print(type(var))


#           ***************** ПРОВЕРКА NONE ***********************

# Для того, чтобы проверить значение переменной на None, мы используем либо оператор is, либо оператор проверки на равенство ==.

# var = None
# if var is None:  # используем оператор is
#   print('None')
# else:
#   print('Not None')

# var = None
# if var == None:  # используем оператор ==
#   print('None')
# else:
#   print('Not None')


#       ********** СРАВНЕНИЕ NONE С ДРУГИМИ ТИПАМИ ДАННЫХ   **************

# Сравнение None с любым объектом, отличным от None, дает значение False

# print(None == None)
# print(None == 17)
# print(None == 3.14)
# print(None == True)
# print(None == [1, 2, 3])
# print(None == 'Beegeek')
# print(None == 0)
# print(None == False)
# print(None == '')

# Сравнивать None с другими типами данных можно только на равенство.

# ****************************  ПРИМЕЧАНИЕ  ************************
# Обратите внимание, что функции, не возвращающие значений, на самом деле, в Python возвращают значение None

def print_message() :
    print('Я - Тимур,')
    print('король матана. ')

print_message()
print(type(print_message()))
res = print_message()