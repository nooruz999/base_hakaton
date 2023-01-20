# file = open('text.txt', mode= 'r', encoding='utf-8')
# print(file.read())
# file.close()

# ggg = 'Umar'
# # file = open('text.txt', mode= 'r', encoding='utf-8')
# with open('text.txt', mode= 'r', encoding='utf-8') as f:
#     content = f.read()
# for name in content:
#     if name.find(ggg) ==-1:
#         print('парнишка найден')
#     else:
#         print('no')


#1

# b='''domashka.py      if_elif.py      open_with_open   set_dict.py   Zadaniya.py   Загрузки      Общедоступные
#  first.py         ifelif.py       second.py        snap          Видео         Изображения  'Рабочий стол'
#  forandwhile.py   list_tuple.py   set_dict         str.py        Документы     Музыка        Шаблоны'''

# a = open ('directories.txt', mode= 'w', encoding='utf-8')
# a.write(b)
# a.close()

#2

# login = input('логин: ')
# password = input('пароль: ')
# regis = open('users.txt', mode='a', encoding='utf-8')
# regis.write('Login  ' + login + '\n')
# regis.write('Password  ' + password + '\n')
# regis.close()

#3

# a = open('text.txt', mode='r', encoding='utf-8')
# for i in a:
#     if 'w' in a:
#         print('DA')
#     else:
#         print('NET')

#4

# b = '''Python is a widely used high-level programming language for general-purpose
# programming, created by Guido van Rossum and first released in 1991. An interpreted
# language, Python has a design philosophy that emphasizes code readability (notably
# using whitespace indentation to delimit code blocks rather than curly brackets or
# keywords), and a syntax that allows programmers to express concepts in fewer lines of
# code than might be used in languages such as C++ or Java.'''

# a = open('python.txt', mode='w', encoding='utf-8')
# a.write(b)
# a.close()

# c = open('python.txt', mode='r', encoding='utf-8')
# r = c.read().split()
# t_words = []
# for letter in r:
#     if 't' in letter or 'T' in letter:
#         t_words.append(letter)
# print(t_words)

#5

