a = int(input("Введите число от 1 до 99"))
first_digit = a % 10
second_digit = a // 10
s = first_digit + second_digit
print(s)