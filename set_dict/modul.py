# # modul OS
# import os 
# # print(os.name)
# # print(os.getlogin())
# # print(os.uname())

# # modul sys
# # модуль sys Модуль sys обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором python.
# import sys
# # print(sys.platform)
# # print(sys.argv)
# # print(sys.version)
# # print(sys.copyright)

# modul datetime
# from datetime import *

# print(datetime.now())
# print(datetime.today())
# a = datetime(2023,1,13,19,1,12)
# print(a)
# b = time(11,34,56)
# print(b)
# c = time(hour=11,minute=33,second=12)
# print(c)

# import time
# print('Agil')
# time.sleep(5)
# print('hello')

# for i in range(5):
#     print('Agil')
#     time.sleep(3)

# d = date(2023,1,13)
# print(d)

# inform = datetime(2023,1,13,19,14,13)
# print('year=',inform.year)
# print('month=',inform.month)
# print('hour=',inform.hour)
# print('minute=',inform.minute)

# from datetime import *

# now = datetime.now()
# # t = now.strftime('%H:%M:%S')
# # print('Time', t)

# s = now.strftime('%A,%Y,%m,%d,%P,%R,%X')
# print(s)

# modul random

# import random

# my_list = ['sdsd','sdsd','dsdsd','sdsd']
# random.shuffle(my_list)
# print(my_list)
# print(random.choice(my_list))

# print(random.randint(1,50))
# print(random.randrange(0,12,2))

# print(random.random())

# module urlib.request

# import urllib.request

# response = urllib.request.urlopen('https://www.itcbootcamp.com/#/')
# print(response.read())
# print(response.getcode())

# import csv
# with open('students.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["ID", "Name", "Duration"])
#     writer.writerow([1, 'Aktan', 'Python'])
#     writer.writerow([2, 'Dima', 'JS'])
#     writer.writerow([3, 'Amal', 'Flutter'])

# modul MATH
# from math import *
# print(pi)
# #import math
# print(math.acos())
# print(math.sin(180))
# print(math.ceil(9.1))
# print(math.floor(9.7))
# print(math.comb(8,5))
# s=True
# print(math.isfinite(s))

# modul secrets

# import secrets
# token = secrets.token_hex(2)
# print(token)

# elem = secrets.choice([21,'ff',43,True])
# print(elem)

# modul collections
# import collections
# c = collections.Counter()
# for word in ['fdgdfg','dfgdf','dfgdfgwefdc','dsfdsfsgrfb']:
    # c[wors] +=1
# print(c)

# from my_module import a
# a

# import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# another_names = []
# # print(random.sample(names, 4))
# another_names = random.sample(names, 4)
# print(another_names)

# import sys
# print(sys.platform)

# import os
# directory = 'Dlya primera'
# parent_dir = 'home/nooruz/Desktop'
# path = os.path.join(parent_dir, directory)
# os.makedirs(path)
# from pathlib import Path

# Path ('home/nooruz/Desktop/Dlya primera').touch()
# Path ('home/nooruz/Desktop/Dlya primera').touch()
# Path ('home/nooruz/Desktop/Dlya primera').touch()
# Path ('home/nooruz/Desktop/Dlya primera').touch()
# Path ('home/nooruz/Desktop/Dlya primera').touch()

# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
