print("z - чайник ")
first = float(input())
symbol = input()
second = float(input())
if symbol == "+":
  result = first + second
if symbol =="-":
  result = first - second
if symbol =="*":
  result = first * second
if symbol =="/":
  result = first / second
print(first, second, "=", result)
if second =="0":
  result = first * second
  result = first / second
print ("не верное значение переменной")