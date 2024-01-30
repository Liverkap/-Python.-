# КОЛИЧЕСТВО СТРОК В ФАЙЛЕ
#
# with open(input(), encoding='utf-8') as file:
#     content = file.readlines()
#     print(len(content))


# СУММАРНАЯ СТОИМОСТЬ

# with open('ledger.txt', encoding='utf-8') as file:
#     content = sum([int(el.strip('$\n')) for el in file.readlines()])
#     print(f'${content}')


# GOOOOOOOOOD STUDENTS

# with open('grades.txt', encoding='utf-8') as file:
#     content = [el.split() for el in file.readlines()]
#     count = 0
#     for el in content:
#         name, t1, t2, t3 = el
#         if int(t1) >= 65 and int(t2) >= 65 and int(t3) >= 65:
#             count += 1
#
#     print(count)


# САМОЕ ДЛИННОЕ СЛОВО В ФАЙЛЕ

# with open('words.txt', encoding='utf-8') as file:
#     content = file.readline().split()
#     max_len = len(max(content, key=len))
#     new_list = list(filter(lambda x: len(x) == max_len, content))
#     print(*new_list, sep='\n')


# TAIL OF A FILE

# with open(input(), encoding='utf-8') as file:
#     content = file.readlines()[-10:]
#
#     for el in content:
#         print(el.rstrip())


#FORBIDDEN WORDS

# with open('forbidden_words.txt', encoding='utf-8') as check:
#     bad_words = {el: '*' * len(el) for el in check.readline().split()}
#     with open(input(), encoding='utf-8') as file:
#         s = ''.join(file.readlines())
#         s_lower = s.lower()
#
#         for el in bad_words:
#             if el in s_lower:
#                 s_lower = s_lower.replace(el, bad_words[el])
#         new_list = list(map(lambda c1, c2: '*' if c2 == '*' else c1, s, s_lower))
#         print(*new_list, sep='')


# ТРАНСЛИТЕРАЦИЯ

# dictionary = {
#     'а': 'a',
#     'б': 'b',
#     'в': 'v',
#     'г': 'g',
#     'д': 'd',
#     'е': 'e',
#     'ё': 'jo',
#     'ж': 'zh',
#     'з': 'z',
#     'и': 'i',
#     'й': 'j',
#     'к': 'k',
#     'л': 'l',
#     'м': 'm',
#     'н': 'n',
#     'о': 'o',
#     'п': 'p',
#     'р': 'r',
#     'с': 's',
#     'т': 't',
#     'у': 'u',
#     'ф': 'f',
#     'х': 'h',
#     'ц': 'c',
#     'ч': 'ch',
#     'ш': 'sh',
#     'щ': 'shh',
#     'ъ': '*',
#     'ы': 'y',
#     'ь': '\'',
#     'э': 'je',
#     'ю': 'ju',
#     'я': 'ya',
#     'А': 'A',
#     'Б': 'B',
#     'В': 'V',
#     'Г': 'G',
#     'Д': 'D',
#     'Е': 'E',
#     'Ё': 'Jo',
#     'Ж': 'Zh',
#     'З': 'Z',
#     'И': 'I',
#     'Й': 'J',
#     'К': 'K',
#     'Л': 'L',
#     'М': 'M',
#     'Н': 'N',
#     'О': 'O',
#     'П': 'P',
#     'Р': 'R',
#     'С': 'S',
#     'Т': 'T',
#     'У': 'U',
#     'Ф': 'F',
#     'Х': 'H',
#     'Ц': 'C',
#     'Ч': 'Ch',
#     'Ш': 'Sh',
#     'Щ': 'Shh',
#     'Ъ': '*',
#     'Ы': 'y',
#     'Ь': '\'',
#     'Э': 'Je',
#     'Ю': 'Ju',
#     'Я': 'Ya'
# }
#
## with open('cyrillic.txt', encoding='utf-8') as file, open('transliteration.txt', 'w', encoding='utf-8') as final:
#     line_1 = file.readline()
#     line_2 = file.readline()
#     for el in line_1.split():
#         word = ''
#         for ch in el:
#             if ch in dictionary:
#                 word += dictionary[ch]
#             else:
#                 word += ch
#
#         print(word, end=' ', file=final)
#     print('\n' + line_2, file=final)


# ТРАНСЛИТЕРАЦИЯ(ОТ ПОЛЬЗОВАТЕЛЯ)
# d = {'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch', 'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*', 'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je', 'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya', 'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch', 'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*', 'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je', 'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya' }
#
# with open('cyrillic.txt', encoding='utf-8') as infile, open('transliteration.txt', 'w', encoding='utf-8') as outfile:
#     text = infile.read()
#     for c in d:
#         if c in text:
#             text = text.replace(c, d[c])
#     outfile.writelines(text)






# ПРОПУЩЕННЫЕ КОММЕНТЫ

# with open(input(), encoding='utf-8') as file:
#     content = file.readlines()
#     new_list = []
#     for i in range(len(content)):
#         if content[i].startswith('def '):
#             if not content[i - 1].startswith('#'):
#                 new_list.append(content[i][4:content[i].find('(')])
#
#     if not new_list:
#         print('Best Programming Team')
#     else:
#         print(*new_list, sep='\n')

# ПРОПУЩЕННЫЕ КОММЕНТЫ(ОТ ПОЛЬЗОВАТЕЛЯ)

# with open(input(), encoding='utf-8') as inf:
# 	not_commented_funcs, preline = [], ''
# 	for line in inf:
# 		if not preline.startswith('#') and line.startswith('def '):
# 			not_commented_funcs.append(line[4:line.find('(')])
# 		preline = line
# 	print('\n'.join(not_commented_funcs) if not_commented_funcs else 'Best Programming Team')