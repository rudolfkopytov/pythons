import string
a = " строка , в которой есть несколько слов(!)"
word = a.split()
word = [word.strip(string.punctuation)for word in word]
print(word)