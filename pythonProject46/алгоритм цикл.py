он походит по всем элементам массива
while (условие) do - это цикл - пока (к примеру не вsgjkybnmcz то или иное условие
    и for
    Пример:


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

    s = Stack()
    s.push(54)
    s.push(45)
    s.push("+")
    while not s.is_empty():
        print(s.pop())