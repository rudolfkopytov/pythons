position=[[0,1,2],[0,4,8],[2,4,6]]
ticket1=[0,1,3,5,5,6]
for p in positions:
    if len(set(ticket1).intersection(set(p)))==3:
        print(f"Ticket{ticket} is win!")

    a=set([1,2,3,4])
    b=([3,4,5,6])
    print(a&b)
    print(a|b)
    print(a.union(b))
    print(a.difference(b))
    print(b.difference(a))
