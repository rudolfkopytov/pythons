a = [3,2,1,-5,4,3,6,7,-3,-5,9,1]
s = a[0]
for x in a:
    if x < s:
        s = x
print(s)