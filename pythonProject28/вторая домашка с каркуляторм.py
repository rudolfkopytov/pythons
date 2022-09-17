sing = input("Enter a sing(+,-,* or /)")

if sing in ["+","-","*","/"]:
    try:
        a = float(input("Enter the first number:"))
        b = float(input("Enter the second number:"))
    except ValueError:
        print(" You have entered not a number")
    else:
        if sing =="+":
            print(a+b)
        elif sing == "-":
            print(a-b)
        elif sing =="*":
            print(a*b)
        elif sing == "/":
            print(a/b)
else: print("Wrong sing")