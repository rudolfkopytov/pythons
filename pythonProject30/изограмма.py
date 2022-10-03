#def is_isogram(string):
#    string = string.lower()
#    for letter in string:
#        if string.count(letter) > 1: return False
#    return True
#print(is_isogram('Dermatoglyphics'))# - код рабочий!

def is_isogram(string):
    return len(set(string.lower())) == len (string)# len - узнаёт величину строки , а SET - это множество.
print(is_isogram('Dermatoglyphics'))
