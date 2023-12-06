# ГЕНЕРАТОРЫ МНОЖЕСТВ

# digits = {int(c) for c in input()}

#                                       {выражение for переменная in последовательность}
# где  выражение — некоторое выражение, как правило, зависящее от использованной в списочном выражении переменной,
# которым будут заполнены элементы множества переменная — имя некоторой переменной, последовательность — последовательность
# значений, которые она принимает (любой итерируемый объект).


#                                       Примеры использования генератора множеств

# squares = {i ** 2 for i in range(10)}
# print(squares)
#
# cubes = {i ** 3 for i in range(10, 21)}
# print(cubes)
#
# chars = {c for c in 'abcdefg'}
# print(chars)


#           **********      В генераторах множеств можно использовать условный оператор!!!!
# digits = {int(d) for d in 'abcd12ef78ghj90' if d.isdigit()}


# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
#
# myset = {int(el) for el in items}
#
# print(*sorted(myset))


# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
#
# myset = {el[:1].lower() for el in words}
#
# print(*sorted(myset))

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a
#  pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if
#   you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know
#    those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and
#    traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
#
# myset = {el.strip(',.:;!?()\n ') for el in sentence.lower().split()}
# print(*sorted(myset))


# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a
#  pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if
#   you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know
#    those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and
#    traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
#
# newset = {el.strip(',.:;!?()\n ') for el in sentence.lower().split()}
# myset = set()
# for el in newset:
#     if len(el) < 4:
#         myset.add(el)
#
# print(*sorted(myset))


# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a
# pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if
# you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know
#  those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and
#  traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
#
# s = {i.strip('.,:():;!?').lower() for i in sentence.split() if len(i.strip('.,:():;!?')) < 4}
# print(*sorted(s))


# files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT',
#          'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py',
#          'stepik.org', 'kotlin.ko', 'github.git']
#
#
# myset = {el.lower() for el in files if el.lower().endswith('png')}
#
# print(*sorted(myset))


#       *********************   FROZENSET   ***********************

# myset1 = frozenset({1, 2, 3})                         # на основе множества
# myset2 = frozenset([1, 1, 2, 3, 4, 4, 4, 5, 6, 6])    # на основе списка
# myset3 = frozenset('aabcccddee')                      # на основе строки
#
# print(myset1)
# print(myset2)
# print(myset3)


#       ********************        Операции над замороженными множествами  *****

# объединение множеств: метод union() или оператор |;
# пересечение множеств: метод intersection() или оператор &;
# разность множеств: метод difference() или оператор -;
# симметрическая разность множеств: метод symmetric_difference() или оператор ^.



# sentence = 'The cat in the hat had two sidekicks, thing one and thing two.'
#
# words = sentence.lower().replace('.', '').replace(',', '').split()
#
# vowels = ['a', 'e', 'i', 'o', 'u']
#
# consonants = {frozenset({letter for letter in word if letter not in vowels}) for word in words}
#
# print(*consonants, sep='\n')


#
# myset1 = set('qwerty')
# myset2 = frozenset('qwerty')
#
# print(myset1 == myset2)