# def recursia(value):
#     print(value)
#     if value < 10:
#         recursia(value+1)
#     print(value)
# recursia(1)

# lambda - фунция (фнонимная, можно не присваивать ссылку на объект, не имеет место в памяти, подходит для легкиъ математич. задач)
# def f(x):
#     return x ** 2 
# print(f(3))

# nurzada = lambda x: x ** 2
# print(nurzada(3))

# aaa = lambda a,b,c: a+b+c
# print(aaa(3,2,5))

# def recursia(avlue):
#     print(avlue)
#     if avlue < 10:
#         recursia(avlue+1)
#     print(avlue)

# recursia(1)


# lambda - функция(анонимная,можно не присваивать ссылку на обьект, не имеет место в памяти,
# подходит для легких математических задач)
# def f(x):
#     return x **2
# print(f(3))
# aaa = lambda x: x**2
# print(aaa(3))


# aaa = lambda a,b,c: a+b+c
# print(aaa(2,3,4))

# def fun_decorator(func):  #параметр Func ссылка на некую функцию
#     def wrapper():
#         print("яячто то делаю до вызова")
        
#         print("яя что то делаю после вызова ")
#         func()
#     return wrapper

# def some_func():
#     print("вызов функции")

# f = fun_decorator(some_func)
# f()

#1
# volume = lambda a,b,c: a*b*c
# pool = 'Объем бассейна'
# print(pool,volume(20,30,40))

#2
# today = lambda a: 365 - a
# data = int(input(':'))
# print(today(data))

#3
# def nechet(a):
#     print(a)
#     if a == 100:
#         return a
#     else:
#         nechet(a+2)
# nechet(1)

#4
# def lset(a):
#     if a == set():
#         return a
#     else:
#         print(a.pop())
#         return lset(a)
# print(lset(a={'admin', 'admin2', 'admin3'}))

#5
# import random
# def aaa():
#     a = []
#     b = random.randrange(10,50)
#     i = 10
#     c = 50
#     while i < c:

#     a.append(b)
#     print(a)
# aaa()
