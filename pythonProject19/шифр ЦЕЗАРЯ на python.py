alphabet = "abcdefghijklmnopqrstuvwxyz"
s = "khoor"
result =""
steps = -3

for char in s:
    letter_number = alphabet.find(char)
    letter_number = (letter_number+3) %  len (alphabet)
    encoded_letter = alphabet[letter_number]
    result+= encoded_letter
    print(result)
