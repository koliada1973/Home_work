# Зробіть декоратор для функції func() з задачі 4, яка реалізує функцію  reduce().
from functools import reduce
import random

def decor1(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        print(a)
        return reduce(lambda x, y: x + y, a)
    return wrapper()


def func():
    return tuple(random.randint(0, 100) for i in range(10) )

fd = decor1(func)
print(fd)