# Реалізуйте декоратори з можливістю задання параметрів:
# кратність для задач 4,5
import random
from functools import wraps

# # для задачі 4
# def decor(N):
#     def decor1(func):
#         @wraps(func)
#         def wrapper():
#             a = func()
#             print(a)
#             return tuple(map(lambda x: x if x % N == 0 else None, a))
#         return wrapper
#     return decor1
#
# @decor(3)
# def func():
#     return tuple(random.randint(0, 100) for i in range(10) )
#
# print(func())
#
#
# # для задачі 5
# import random
#
# def decor2(N):
#     def decor1(func):
#         def wrapper(*args, **kwargs):
#             a = func(*args, **kwargs)
#             print(a)
#             return tuple(filter(lambda x: x % 3 == 0, a))
#         return wrapper
#     return decor1
#
# @decor2(3)
# def func():
#     return tuple(random.randint(0, 100) for i in range(10) )
#
#
# print(func())

# кількість запусків функції func() (кортежів) — для задачі 6.
import random

def decor2(N):
    def decor1(func):
        @wraps(func)
        def wrapper():
            l = []
            for i in range(N):
                l.append(func())
                print(l[i])
            args = l
            return tuple(zip(*args))
        return wrapper
    return decor1


@decor2(3)
def func():
    return tuple(random.randint(0, 100) for i in range(10))

print(func())
