primes = []

for p in range(2, 1000):

    is_prime = True
    for i in range(2,p):
        if p % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(p)

print (primes)