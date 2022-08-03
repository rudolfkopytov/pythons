n = int(input())
s = input()

ans = 0
for digit in s:
    ans *=n
    ans += int(digit)

print(ans)
