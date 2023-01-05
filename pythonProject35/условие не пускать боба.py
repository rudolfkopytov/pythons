my_name = (input("input your name:"))
age = int(input("input your age:")) # если хотим преобразовать число в строку, то пишем int
if age > 18 and my_name != 'Bob':# и это работает!- Bob не впускает
    print(f'Hello {my_name}')
elif age == 18:
    print("Ok, come in!")
elif my_name == "Sam":
    print("SAM!!!")# - это не работает , а должно!
else: #if age < 18:-замена второго условия if на else - сокращает сам код.
    print (' Go out')