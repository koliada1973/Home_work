import math

x = [1, 2, 3, 4]
def my_sum(my_list):
    if not my_list:
        return 0
    result = 0
    for i in my_list:
        result += i
    return result
print(f'my_sum([x]): {my_sum(x)}')
print(f'my_sum([]): {my_sum([])}')

print(f'sum(x): {sum(x)}')

result = 0
for i in x:
    result += i
print(f'result: {result}')

from functools import reduce
# help(reduce)
print(f'reduce(lambda a, b: a + b, x): {reduce(lambda a, b: a + b, x)}')
# Нічого не зрозуміло!!! Якщо стартове значення зробити 6, то результат = 16. Чому - не ясно
print(f'reduce(lambda a, b: a + b, x, 6 (6 - стартове значення)): {reduce(lambda a, b: a + b, x, 6)}')

def test_reduce(x, start = 0):
    f = lambda a, b: a + b
    result = start + f(x[0], x[1])
    for i in x[2:]:
        result = f(result, i)
    return result
print(f'test_reduce(x, 5): {test_reduce(x, 5)}')

import random
w = [random.random() for i in range(1000)]
# print(w)
from timeit import timeit
print(f'Time, test_reduce(w), seconds:  {timeit('test_reduce(w)', number=10000, globals = {'test_reduce': test_reduce, 'w':w})}')
print(f'Time, reduce(lambda a, b: a + b, w), seconds:  {timeit('reduce(lambda a, b: a + b, w)', number=10000, globals = {'reduce':reduce, 'w':w})}')

def my_pow(n, power):
    return n**power

from functools import partial
# help(partial)
sqrt = partial(my_pow, power = 0.5)
cubic = partial(my_pow, power = 3)

print(sqrt(9))
print(sqrt(12))
print(cubic(3))