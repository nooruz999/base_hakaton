# a=[1,2,3]
# print(all(a))
# print(any(a))

# num=[1,2,3,4,5]
# print(min(num), max(num))

# print(abs(-66))

#1

# values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
# spisok =[]
# try:
#     for i in values:
#         if set(i):
#             spisok.append(True)
#         else:
#             spisok.append(False)

#         if all(spisok)==True:
#             print('vse konvertiturmye')
#         else:
#             print('byvaet')

# except:
#     print('kkslksldksl')

#2

# try:
#     b=set()
#     i=0
#     while i<5:
#         a=int(input('Введите пять чисел:  '))
#         i+=1
#         b.add(a)
#     print(min(b))

# except ValueError:
#     print('nevozmozhno')

#2.1

# try:
#     a = set()
#     i = 0
#     while i < 5:
#         num = int(input("введите число:  "))
#         i+=1
#         a.add(num)
#     print(min(a))
# except ValueError:
#     print("возможно вы ввели строку") 

#4

# a = int(input('Сумма кредита?:   '))
# b = 3.47
# if a >=50000:
#     print(a*(b/100))