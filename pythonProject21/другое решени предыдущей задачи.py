a = input()

word = a.split()
even_word = word[::2]
s =" ".join(even_word)
print(s)