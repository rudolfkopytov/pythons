class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
#Здесь __init__ — это так называемый «магический» метод-конструктор, окруженный двумя
# нижними подчёркиваниями с обеих сторон. Такие подчёркивания иногда для краткости
# называются дандерами, от «double underscore». Магические методы обычно неявно вызываются
# при совершении каких-либо операций,
peter = User(name="Peter Robertson", email="peterrobertson@mail.com")
julia = User(name="Julia Donaldson", email="juliadonaldson@mail.com")

print(peter.name)
print(julia.email)