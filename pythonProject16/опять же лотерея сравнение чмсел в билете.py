positions=[[0,1,2],[0,4,8],[2,4,6]]
ticket1=[0,1,3,5,5,6]
#ticket1=[0,2,4,5,5,6]#?
for p in positions:
    if len(set(ticket1).intersection(set(p)))==3:#set (ticket1)&set(p)
        print(f'Ticket {ticket1}is win')

a=set([1,2,3,4])
b=set([3,4,5,6])
print(a&b)#?
print(a|b)#?
print(a.union(b))#?
print(a.difference(b))#(1,2)
print(b.difference(a))#?