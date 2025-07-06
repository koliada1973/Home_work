# Створити просту функцію (не приймає жодного параметру) та пару декораторів
# (перший декоратор виводить „before“ та „after“ до та після виконання функції відповідно,
# другий – виводить час виконання функції) (задати опис як для функції так і для внутрішьної функції).
# Застосувати декоратори:
# - через присвоєння змінній
# - через @
# - використавши functools.wraps
# У всіх 3 варіантах вивести (__doc__, __name__) задекорованої функції (як у навчальному відео).

from functools import wraps
def my_decor1(x, y):
    def f1(func):
        @wraps(func)
        def my_wraper(*args, **kwargs):
            """doc string wraper1"""
            print("before.."*x)
            func(*args, **kwargs)
            print("after.."*y)
        return my_wraper
    return f1

import time
def my_decor2(func):
    @wraps(func)
    def my_wraper(*args, **kwargs):
        """doc string wraper2"""
        start = time.time()
        func(*args, **kwargs)
        print(f'start :  {start}')
    return my_wraper

@my_decor2
@my_decor1(2,3)
def simple_func(a):
    """ Опис simple_func..."""
    print(f'Simpl function...{a}')

# x = my_decor2(simple_func)
# x()

simple_func(5)
print(simple_func.__name__)
print(simple_func.__doc__)