my_dict_1 = {
    'name': 'Garry',
    'age' : 28
}
my_dict_2 = {
    'phone' : '+7 911 021 71 38',
    'country': 'Russia'
}
new_dict = {}
for x, y in my_dict_1.keys(), my_dict_1.values():
    new_dict[x] = y

for x, y in my_dict_2.keys(), my_dict_2.values():
    new_dict[x] = y
print(new_dict)# результат : объеденились 2 dicta.