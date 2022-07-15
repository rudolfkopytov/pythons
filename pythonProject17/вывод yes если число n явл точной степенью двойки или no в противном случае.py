N = 128

def check(a):
    if a % 2 == 0:
        return check(a // 2)
    else:
        if a == 1:
            return True
        else:
            return False

print(check(N))
