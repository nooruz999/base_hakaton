# transport = input('какой транспорт вы выбираете: самолет, поезд, автобус:')

# if transport == 'самолет':
#            ticket_type = input('Каким классом вы хотите лететь: эконом, бизнес:')
#         if ticket_type == 'Эконом':
#             place = input('Где бы вы хотели сидеть: у окна, в проходе: ')
#         else:
#             place = 'у вас бизнес зал'

# elif transport == 'поезд':
#     ticket_type = input('Как вы хотите ехать: купе, плацкарт:')
#     if ticket_type == 'купе':
#         place = input('Выберите одно из свободных мест: 12, 55, 77')
#     elif ticket_type == 'плацкарт':
#         print('В плацкарте мест нет')
#         exit()

# elif transport == 'автобус':
#     ticket_type = input('Как вы хотите ехать: сидя, стоя')
#     if ticket_type == 'сидя':
#         place = input('Выберите место: 5, 7, 8')

#     else:
#         place = 'Где удобно'
# else:
#         print('Такого места нет!')
#         exit()

# print('Ок, внесите оплату')
# print(f'Вы выбрали: {transport} ваше место: {place}')

# order = input('Что закажите?: шаурма, самса, пирожок: ')

# if order == 'шаурма':
#     fill_type = input ('Какую начинку хотите?: мясо, курица:')
#     if fill_type == 'мясо':
#         amount = input ('Сколько хотите?: ')
#     elif fill_type == 'курица':
#         amount = input ('Сколько хотите?: ')

# elif order == 'самса':
#     fill_type = input ('Какую начинку хотите?: мясо, курица, сыр: ')
#     if fill_type == 'мясо':
#         amount = input ('Сколько хотите?: ')
#     elif fill_type == 'курица':
#         amount = input ('Сколько хотите?: ')
#     elif fill_type == 'сыр':
#         waiting = input ('Они закончиличь, будете ждать 15 мин?: да, нет: ')
#         if waiting == 'да':
#             print('Спасибо за ожидание')
#         else:
#             print('Спасибо. До свидание')
#             exit()
# elif order == 'пирожок':
#     fill_type == input ('Какую начинку хотите?: капуста , картошка: ')
#     if fill_type == 'капуста':
#         amount = input ('Сколько хотите?: ')
#     elif fill_type == 'картошка':
#         amount = input ('Сколько хотите?: ')

# print('Ок, внесите оплату')
# print(f'Ваш заказ {order}, начинка {fill_type}, количество {amount}')

# transport = input('какой транспорт вы выбираете: смолет, поезд, автобус: ')

# if transport == 'смолет':
#     ticket_type = input('Каким классом вы хотите лететь: эконом, бизнес: ')
#     if ticket_type == 'эконя ом':
#         place = input('Где бы вы хотели сидеть: у окна, в проходе: ')
#     else:
#         place = 'у вас бизнес зал'

# elif transport == 'поезд':
#     ticket_type = input('Как вы хотите ехать: купе, плацкарт: ')
#     if ticket_type == 'купе':
#         place = input('Выберите одно из свободных мест: 12, 55, 77')
#     elif ticket_type == 'плацкарт':
#         print('В плацкарте мест не осталось!')
#         exit()


# elif transport == 'автобус':
#     ticket_type = input('Как вы хотите ехать: сидя, стоя')
#     if ticket_type == 'сидя':
#         place = input('Выберите место: 5, 7, 8')
    
#     else:
#         place = 'Где угодно'
# else:
#     print('Такого транспорта нет!')
#     exit()


# print('Ок, внесите оплату')    
# print(f'Вы выбрали: {transport} ваше место: {place}')    
    
# food_choise = input('Что закажете: шаурма, самса, пирожок: ')
# if food_choise == 'шаурма':
#     filling = input('Какую начинку хотите: мясо, курица: ')
# elif food_choise == 'пирожок':
#     filling = input('Какую начинку вы хотите: картошка, капуста: ')
# elif food_choise == 'самса':
#     filling = input('Какую начинку вы хотите: мясо, курица, сыр: ')
#     if filling == 'сыр':
#         choise = input('Самсы с сыром закончились, будете ждать: да, нет: ')
#         if choise == 'нет':
#             exit()
# else:
#     print('Такого блюда нет!')
#     exit()

# how_much = input('Сколько хотите: ')
# warm = input('Нужно ли разогреть: да, нет: ')
# drink = input('Что будете пить: чай, кофе, кола, минералка: ')
# if drink == '':
#     print('Вы заказали', food_choise, filling, how_much, ',', 'клиент напиток не взял')
# else:
#     print('Вы заказали', food_choise, 'c', filling, how_much, 'шт',',', drink)
