s = "z"
result = ""
steps = 3


for char in s:
    letter_number = ord(char) - ord("a")
    letter_number = (letter_number + steps) % 26
    encoded_letter = chr(ord("a")+ letter_number)
    result += encoded_letter
print(result)