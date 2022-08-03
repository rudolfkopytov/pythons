n = int(input())
isprime = True
for div in range(2,n):
    if n % div == 0:
        isprime = False

if isprime:
    print(f" Число {n} является простым")
else:
    print(f" Число {n} не является простым")