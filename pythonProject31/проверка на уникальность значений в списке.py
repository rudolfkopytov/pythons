my_list =[1,2,3,4,5,5,6,7,8,5,4]
print(len(my_list) == len(set(my_list)))# False (потомучто 5 и некоторые цифры повтряются двыжды, без них в списке он выведет True
#самый простой способ найти уникальные значения через метод len -длинну списка