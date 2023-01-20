# return

# def hello():
#     return 'Agil where are you?'
# # messege = hello()
# # print(messege)
# print(hello())

# def sum(a,b):
#     return a + b
# print(sum(2,5))

# def square(x):
#     return x ** 2
# print(square(3))

# def get_max(a,b):
#     return a if a > b else b
# print(get_max(2,6))

# from math import *

# def cylinder():
#     r = float(input(':   '))
#     h = float(input(':   '))
#     side = (2 * pi * r * h) # площадь боковой поверхности
#     circle = pi * r ** 2
#     full = side + 2 * circle
#     return full, side, circle
# print(cylinder())

#  *args and **kwargs

# def name(*args):
#     for i in args:
#         return i
# word =("kak dela s funkciyami?")

# print(name(word))


# def find_animal(*args):
#     if "dog" in args:
#         return True
# print(find_animal("cat","mouse",12,32,False,"dog"))

# def infor(game, **kwargs):
#     players = []
#     numbers = []
#     if game =="football":
#         for k,w in kwargs.items():
#             players.append(k)
#             numbers.append(w)
#         return game,players,numbers
# print(infor(game = "football",alex = "first", bob = "second",messi = "ten",ronaldo = "seven"))

# def phone_book(**kwargs):
#     name = []
#     phone = []
#     for k,v in kwargs.items():
#         name.append(k)
#         phone.append(v)
#     return name,phone
# print(phone_book(agil = "+9969379992", egida = "+996love"))

#1
# from math import *

# def add(a,b):
#     return a+b
# print(add(5,10))
# def substract(a,b):
#     return a-b
# print(substract(5,10))
# def multiply(a,b):
#     return a*b
# print(multiply(5,10))
# def divide(a,b):
#     return a/b
# print(divide(5,10))

#2
# message = input("строка")
# sum = 0
# def fffff():
#     global message
#     global sum
#     for i in message:
#         sum+=1
#     return sum
# print(fffff())

# def count_sym(txt):
#   result = 0
#   for char in txt:
#     result += 1
#   return result
        
# print(count_sym("hello people my name is Giorgio Armani"))

#3

# def dict(a,b):
#     a.update(b)
#     return a 
# a = {input("a: "): input("b: ")}
# b = {input("new: "): input("new2: ")}
# print(dict(a,b))

#4

# a = input('покушать: ')
# b = input('выпить: ')

# def zakaz(a,b):
#     c = open('menu.txt', mode='w', encoding='utf-8')
#     c.write(a)
#     c.write(b)
#     return c
# print(zakaz(a,'\n' + b))

#5

# def new_file():
#     a = input(':')
#     c = open(f'{a}.py', mode='w', encoding='utf-8')
#     return c
# print(new_file())

#6

# def prime():
#     print("Я главная функция")
#     def nested():
#         print("Я вложенная функция")
#     nested()
# prime()

#7

# def dict(*args):
#     for i in args:
#         a = tuple(i.keys())
#         b = tuple(i.values())
#     print(a,b)

# dict({'color': 'blue', 'fruit': 'apple', 'pet': 'dog'})

# #8
# def simple():
#     n = int(input())
#     prime = True
#     i = 2
#     while i < n:
#         if n % i == 0:
#             prime = False
#         i += 1
#     if prime:
#         print('Простое')
#     else:
#         print('Сложное')
# simple()

# def new(a,b):
#     a = list(a)
#     b = list
