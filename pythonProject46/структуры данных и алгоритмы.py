def encrypt(string):

    alf = ('а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я')
    new = []
    for i in string:
        if i not in alf:
            new.append(i)
        else:
            if  i == 'я':
                new.append('а')
            else:
                new.append(alf[alf.index(i)+1])
    return " ".join(new)
word = input('Введите слово для шифрования')
print(encrypt(word))
class Node:
    def __init__(self, cargo=None, next=None, back=None):
        self.cargo = cargo
        self.next  = next
        self.back = back

    def __str__(self):
        return str(self.cargo)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node = Node("test")

print(node)