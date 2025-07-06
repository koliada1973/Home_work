from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not work:
            return "Функція не працює.."
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function():
    return "Функція працює.."

work = True
print(my_function())

work = False
print(my_function())
