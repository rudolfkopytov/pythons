email = "admin@mail.ru"

at_index = None
for i in range(len(email)):
    if email[i] =="@":
        at_index = i

ans = email[at_index +1:]

print(ans)
