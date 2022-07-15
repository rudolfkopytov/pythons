m = 144

for p in primes:
    while m % p ==0:
        print(p)
        m = m // p
print (m)
