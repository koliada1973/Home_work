# Зробіть декоратор для функції func() з задачі 4, який відфільтровує значення, кратні 3.
# Використати функцію filter() та lambda.

import random

def decor1(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        print(a)
        return tuple(filter(lambda x: x % 3 == 0, a))
    return wrapper


def func():
    return tuple(random.randint(0, 100) for i in range(10) )

fd = decor1(func)
print(fd())