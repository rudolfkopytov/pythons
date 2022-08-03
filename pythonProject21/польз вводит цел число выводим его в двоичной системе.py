number = 236

ans = ""
while number:
    if number % 2 == 0:
        ans = "0" + ans
    else :
        ans = "1" + ans
    number = number // 2
print(ans)