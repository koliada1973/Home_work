# Зробіть декоратор для функції func() з задачі 4, який запускає дану функцію 2 рази,
# а потім повертає результат при допомозі zip (об“єднує отримані в результаті запусків кортежі).

import random

def decor1(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        b = func(*args, **kwargs)
        print(a)
        print(b)
        return tuple(zip(a, b))
    return wrapper()


def func():
    return tuple(random.randint(0, 100) for i in range(10) )

fd = decor1(func)
print(fd)