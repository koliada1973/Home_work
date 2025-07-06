# Задача 4.
#  Нехай в нас є функція func(), яка повертає кортеж 10-ти цілих чисел в діапазоні 0 до 100.
#  Зробіть декоратор з використанням функцій map, lambda.
#  Задекорована функція повинна числа, кратні 2, залишати без змін, всі інші числа замінити на None.


import random

def decor(func):
    def wrapper(*args, **kwargs):
        Y = tuple(func(*args, **kwargs))
        print(Y)
        return tuple((map(lambda i: i if i % 2== 0 else None, Y )))
    return wrapper

# @decor
def func():
    return (random.randint(0,100) for i in range(10) )

A = decor(func)


print(A())