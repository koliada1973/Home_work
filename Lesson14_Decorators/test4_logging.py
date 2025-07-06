from functools import wraps

def logit(func):
    @wraps(func)
    def my_logging(*args, **kwargs):
        print("Була викликана функція ", func.__name__)
        return func(*args, **kwargs)
    return my_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x

result = addition_func(4)
print(result)