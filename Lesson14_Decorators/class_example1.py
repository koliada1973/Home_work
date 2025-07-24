# Створити просту функцію (не приймає жодного параметру) та пару декораторів (перший декоратор виводить „before“ та „after“ до та після виконання функції відповідно, другий – виводить час виконання функції) (задати опис як для функції так і для внутрішьної функції).
# Застосувати декоратори:
# - через присвоєння змінній
# - через @
# - використавши functools.wraps
# У всіх 3 варіантах вивести (__doc__, __name__) задекорованої функції (як у навчальному відео).

from functools import wraps
import time

def decor1(x, y):
    def decor(func):
        """docstring decor"""
        @wraps(func)
        def wrapper(a):
            print('before func1' * x)
            func(a)
            print('after func1' * y)
        return wrapper
    return decor

def decor2(func):
    """docstring decor2"""
    @wraps(func)
    def wrapper(a):
        start = time.time()
        func(a)
        print(f'start :  {start}')
    return wrapper

@decor1(2, 3)
@decor2
def func1(a):
    """docstring func1"""
    print("i'm simple function" * a)

# dec_func1 = decor1(func1)
# dec_func1()

func1(3)
print(func1.__doc__, func1.__name__)