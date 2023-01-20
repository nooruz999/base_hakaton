# 1 Используя обработчик ошибок создайте калькулятор
# 2 используя цикл while
# 3 который можно использовать бесконечно, при условие если 
# сам пользователь не захочет его остановить
# 'Хотите продолжить? 1-Да  2-Нет
# 4 обработчик ошибок должен проверять на деление 
# на ноль и введение строки вместо чисел

# #Калькулятор

# try:
#     while True:
#         num_1=int(input('Первое число ?:  '))
#         num_2=int(input('Второе число ?:  '))
#         task=input('Знак?: *,/,+,-  ')
        
#         if task == '*':
#             print(num_1*num_2)
#         elif task == '/':
#             print(num_1/num_2)
#         elif task == '+':
#             print(num_1+num_2)
#         elif task == '-':
#             print(num_1-num_2)
#         cont = input('Хотите продолжить?: Да, Нет  ')
#         if cont == 'Да':
#             continue
#         elif cont == 'Нет':
#             break
# except ZeroDivisionError:
#     print('Ошибка ноля!!!!')
# except ValueError:
#     print('Только цифры!!!')

# #Calc

# try:
#     while True:
#         num1 = int(input("first number:   "))
#         num2 = int(input("second number:   "))
#         operation = input("choose operation +,-,/,*:   ")
#         if operation == "+":
#             print(num1+num2)
#         elif operation == "-":
#             print(num1-num2)
#         elif operation == "/":
#             print(num1 / num2)
#         elif operation == "*":
#             print(num1 * num2)
#         if input("ходите продолжить - да или - нет:   ") == "да":
#             True
#         else:
#             break
# except ZeroDivisionError:
#     print("на ноль делить нельзя")
# except ValueError:
#     print("введи корректные данные ")

# while True:
#     try:
#         num1 = int(input("first number:   "))
#         num2 = int(input("second number:   "))
#         operation = input("choose operation +,-,/,*:   ")
#         if operation == "+":
#             print(num1+num2)
#         elif operation == "-":
#             print(num1-num2)
#         elif operation == "/":
#             print(num1 / num2)
#         elif operation == "*":
#             print(num1 * num2)
#         # if input("ходните продолжить - да или - нет") == "да":
#         #     True
#         # else:
#         #     break
#     except ZeroDivisionError:
#         print("на ноль делить нельзя")
#     except ValueError:
#         print("введи корректные данные")
#     if input("ходните продолжить - да или - нет") == "да":
#         True
#     else:
#         break


#

# 1 У пользователя запрашивается предложение в бесконечном режиме
# 2 Если длина предложения меньше 6 слов, то нужно продолжить
# 3 Если больше шести, выводит на экран и прерывает цикл

# while True:
#     text = input('Введите предложение меньше 6 слов: ')
#     c = len(text.split())
#     if c < 6:
#         print("c < 6")
       
        
#     elif c > 6:

#         print("c > 6")
#         break

# Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована;
# Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран;
# Даны три числа. Вывести на экран «yes«, если среди них есть одинаковые, иначе вывести “ERROR”;
# Даны три числа. Вывести на экран «yes«, если можно взять какие-то два из них и в сумме получить третье;
# Дано три числа. Найти количество положительных чисел среди них;
# Вывести на экран все чётные значения в диапазоне от 1 до 497;
# Посчитать сумму числового ряда от 0 до 14 включительно. Например, 0+1+2+3+…+14;
# Перемножить все не чётные значения в диапазоне от 0 до 9435;
# Записать в массив все числа в диапазоне от 54 до 9184 кратные 5;

# a=[0,0,0,0,0,0,0]
# for k,i in enumerate(a, 1):
#     print(k,i)

# a=[0,0,0,0,0,0]
# b=1
# for i in a:
#     print(b,i)
#     b+=1

# summ=0
# i=0
# while i<=100:
#     summ+=i
#     i+=1
#     print(summ)


