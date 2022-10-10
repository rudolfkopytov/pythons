height = int(input())
width = int(input())
result_array = []
for x in range(height):
    s = []
    for y in range(width):
        s.append([])
    result_array.append(s)
print(result_array)# на симуляторе это работает если начать с 2-ки и далее с новой строки 3