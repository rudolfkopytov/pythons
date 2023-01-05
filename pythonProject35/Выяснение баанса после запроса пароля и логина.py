balance = 35000
login = input("Login: ")
password = input("Password: ")
account = { 'log':'admin', 'pas': '1234'}

if login == account['log'] and password == account['pas']:
    print(f'Hello {login}\nYour balance: {balance}')
else:
    print("Permission is denied")