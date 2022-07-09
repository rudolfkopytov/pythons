def f(a, b=2):
    return a + b
print(f(3,4))
print(f(3))

def f2 (*args):
    res=0
    for i in args:
        res+=i
    return res

print(f2(3,4))
print(f2(3))
print(f2(3,4,5,6,7,8))

