a =[1,2,3,4,5,]

def _sum(a: list):
    s = 0
    for x in a:
        s += x
    return s
s = _sum(a)
print(a)