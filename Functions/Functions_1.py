#1 def... <name>(args):

#         <body>
#       print('logic')
#   <name>(......)

# def send_text():
#     text = 'Мы наконец-то создали данную функцию'
#     print(text)
# send_text()

# def counter():
#     a = int(input(":"))
#     b = int(input(":"))
#     print("total", a+b)
# counter()

# def hello_name(from_name):  # обьязательные параметры
#     text = f'my name is {from_name}'
#     print(text)
# hello_name("agil") # аргументы

# def country(city = "Bishkek"):
#     print("im from " + city)
# country()
# country("Talas")

# Глобальные и локальные переменные
# def num():
#     a,b,c = 1,2,3 # local
#     print(a,b,c)
# num()


# a,b,c = 4,5,6 # global

# num()

# def hi():
#     name = "agil"
#     print(name)

# name = "nooruz"
# hi()

# numbers = [2,3,4,3,5,3,4,5,6,3,4,3,5,5,2,4]
# def num():
#     chet = []
#     nechet = []
#     for i in numbers:
#         if i % 2 == 0:
#             chet.append(i)
#         else:
#             nechet.append(i)
#     print(chet,nechet)
# num()

# def num(numbers = list):
#     a = []
#     b = []
#     for i in numbers:
#         if i % 2 == 0:
#             a.append(i)
#         else:
#             b.append(i)
#     print(a,b)
# num([12,32,13,23,21,312,3,3,5,3,1,8,8,54,2])
# num([23,4,5,2,3,5,2,2,3423,23,4,23,32,])


# def method_1():
#     list_1 = ['name', 'age', '1', '19']
#     x = list_1[1::-1]
#     y = list_1[3:1:-1]
#     print(x+y)
# method_1()

# def fibonacci():
#     f_1 = f_2 = 1
#     a = int(input('num: '))
#     print(f_1, f_2, end=" ")
#     for i in range(2, a):
#         f_1, f_2 = f_2, f_1 + f_2
#         print(f_2, end=' ')
# fibonacci()

# def method_1():
#     a = int(input(":"))
#     b = int(input(":"))
#     c = (a + b, a - b )
#     print(c)
# method_1()

######## def meth(a, b):
#     print(a + b, a - b)
# meth(1,2)

# def method_2():
#     method_1()

# def new_file():
#     name= input(': ')
#     a = open(name,mode='w')
#     a.write('ppc')
#     a.close()
# b = new_file
# print(b())

# import random

# def gen_number():
#     a = random.shuffle(1,4,5,7,9,0)
#     for i in range(a):
#         i = i <= 5
#         print('0444'+i)

# gen_number()

# from random import choice
# def gen_number():
#     i = 0
#     print('0444', end='')
#     while i <= 5:
#         n2 = [1,4,5,7,9,0]
#         print(choice(n2), end='') 
#         i = i + 1
# gen_number()


# def kVt():
#     novoe = int(input())
#     staroe = int(input())
#     if staroe 
