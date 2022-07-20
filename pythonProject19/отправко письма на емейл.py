def send_email(email, text):
    if "@" not in email:
        raise ValueError('Incorrect Email')
try:
    send_email(123@email.com)
except ValueError as e:
    print(e)