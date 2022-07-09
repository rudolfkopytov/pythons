n = 128

def check (a):
    if a % 2 == 0:
        return  check(a // 2)
    else:
        if a == 1:
            return True
        else:
            return False

check(n)
# Дано натуральное число n .
# Выведите слово "yes", если число "n"
# является точной степенью двойки , или слово "no", в противном случае.