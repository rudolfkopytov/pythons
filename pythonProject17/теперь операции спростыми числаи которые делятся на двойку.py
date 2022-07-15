p = 22

is_prime = True
for i in range(2,p):
    if p % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"Число {p} - простое")
else:
    print(f"Число {p} - не простое")