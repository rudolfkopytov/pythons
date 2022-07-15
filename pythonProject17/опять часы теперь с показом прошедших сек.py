n = 10745

s = n % 60

n = n // 60
m = n % 60

h = n // 60

print(f"{h:02d}:{m:02d}:{s:02d}")