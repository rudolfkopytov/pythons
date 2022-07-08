def check_user(username, password):
    if username in user_database:
        if password == user_database[username]:
            return True
        else:
            return False
    else:
        return False
