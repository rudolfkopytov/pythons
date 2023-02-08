my_dict = {
    "first_el" : "aplle",
    "second_el": "banana",
}

#for value in my_dict.values():
    #print(value)# - таким образом мы выводим наименования (сам пароль и логин)
#for value in my_dict.keys():
    #print(value)# таким образом мы выводим значения тех самых логина и пароля
#for value in my_dict. items():
    #print(value)# - этот метод (items ) -выводит и логин и его значение и пароль и его значение!
for key,  value in my_dict. items():
    print(f"{key}----value")# -более наглядный вывод ключа и его значения.
