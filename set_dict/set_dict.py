# a.add()
# a.update()
# a.pop()
# a.remove()
# a.clear()

# country = {"name": "Kyrgyzstan", "city": "Bishkek", "code": 312}
# print(country.get("code"))
# print(country)
# country.popitem()
# print(country.keys())
# print(country.values())
# print(country.items())

#1

# dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6,7}
# dates_of_birth.remove(7)
# print(dates_of_birth)

#2

# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# c = farm_1.intersection(farm_2)
# print(c)

#3

# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# c = farm_1.difference(farm_2)
# print(c)

#4

# farm_1 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_1.add("sheep")
# farm_1.pop()
# print(farm_1)

#000

# menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
# menu.update({'besh_barmak': 130})
# menu['lagman'] = 135
# menu.pop('borsh')
# print(menu)

#10

# menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
# a = ({'drinks': ['sprite', 'fanta', 'cola']})
# menu.update(a)
# print(menu)

#20

# a_set = {'.add', '.remove', '.clear', '.update', '.difference', '.discard','.intersection','.intersection_update', '.pop'}
# b_dict = {'.clear', '.get', '.keys', '.values', '.items', '.update'}
# c = a_set.intersection(b_dict)
# print(c)

#Dop

person = {
    "user1":{
        "name":"ageil",
        "age": 18,
        "adress":["bishkek","neponyatnaya str."],
        "hobby":{"python":"junior","math":"professional"}
    },
    "user2":{
        "name": "nooruz",
        "age": 32,
        "adress":["bishkek", "Dachnaya str."],
        "hobby":{"python":"junior", "math": "non-professional"}
    }
}

print(person ["user1":"adress"])