class Node:
    def __init__(self, cargo=None, next=None, back=None):
        self.cargo = cargo
        self.next  = next
        self.back = back

    def __str__(self):
        return str(self.cargo)# - не работает без предыдущего отдела