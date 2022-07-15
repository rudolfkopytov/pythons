def decorator(func):
    def wrapper():
        result = func()
        ans = ""
        ans += "-" * (len(result) + 2)
        ans += f"\n|{result}|\n"
        ans += "-" * (len(result) + 2)
        return ans

    return wrapper


@decorator
def get_hello():
    return "Hello world!"


print(get_hello())