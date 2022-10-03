#def pallindrome (string):
 #   return string == ''.join(reversed(string))
#print(pallindrome('abba'))

def pallindrome (string):
    return string == string[::-1]
print(pallindrome("abba")) # - это првильней код, хотя проверь сам!