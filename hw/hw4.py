def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

@uppercase
def say_hello():
    return "Привет!"

print(say_hello())
