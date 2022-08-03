A = [1,3,4,4,5,5,6,7]
min_elem = None
for elem in A:
    if min_elem == None or min_elem > elem:
        min_elem = elem

print(min_elem)