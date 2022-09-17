inString = input("Input math expression separated by spaces (example: 2 + 3 * 9 / 10):")
inString = inString.strip()
if not inString:
    exit("input is empty")
prc_string = inString.split(" ")
def is_it_math_symbol(i):
    myMath = ["-", "+", "/", "*"]
    for x in myMath:
        if (i == x):
            return True
    return False
countNum = 0
for i in prc_string:
    if i == " ":
        del prc_string[countNum]
    countNum +=1
countNum = 0
for i in prc_string:
    try:
        n = int(i)
        countNum += 1
    except ValueError:
        if is_it_math_symbol(i):
            countNum += 1
        else:
            print("You input unacceptable symbol: ", i)
            exit()
expression_string = " ".join(prc_string)
print(expression_string, " = ", eval(expression_string))
print()