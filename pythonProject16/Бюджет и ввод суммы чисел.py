budget = 30
my_budget = "мне необходимо %s  для дальнейшего существования" %(budget)
print(my_budget)

string = input("Введите числа через пробел:")

list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # cписок чисел

print(sum(list_of_numbers[::3])) 