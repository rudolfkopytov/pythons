def is_leap_year (x):
    return (x % 400 == 0) or ((x % 4 == 0) and(x % 100 !=0))

print (is_leap_year(2033))# и это работает - сам удостоверься!!