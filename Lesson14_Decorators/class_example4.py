# Задача 4.
#  Нехай в нас є функція func(), яка повертає кортеж 10-ти цілих чисел в діапазоні 0 до 100.
#  Зробіть декоратор з використанням функцій map, lambda.
#  Задекорована функція повинна числа, кратні 2, залишати без змін, всі інші числа замінити на None.

import random


def decor1(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        print(a)
        return tuple(map(lambda x: x if x % 2 == 0 else None, a))
    return wrapper()


def func():
    return tuple(random.randint(0, 100) for i in range(10) )

fd = decor1(func)
print(fd)