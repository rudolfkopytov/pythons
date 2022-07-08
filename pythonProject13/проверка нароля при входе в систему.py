password = {
    "user" : "12345",
    "root" : "10 101",
    "admin":"aaa"
}
password.keys()
password.values()
password.get("user")
# перебор словаря
for name,password in password.items():
    print(name + password)


    