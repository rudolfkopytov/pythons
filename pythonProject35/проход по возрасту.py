my_name = (input("input your name:"))
age = int(input("input your age:")) # если хотим преобразовать число в строку, то пишем int
if age > 18:
    print(f'Hello {my_name}')
else: #if age < 18:-замена второго условия if на else - сокращает сам код.
    print (' Go out')# - работает!