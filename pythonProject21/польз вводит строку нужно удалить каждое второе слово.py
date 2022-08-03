a = input()

word = a.split()

s = ""
for i in range(len(word)):
    if i % 2 == 0:
        s += word[i]
        s += ""
print(s)