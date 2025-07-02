x = [1, 2, 3, 4]
result = []
for i in x:
    result.append(i**2)
print(result)

result = [i**2 for i in x]
print(result)

def sqr(n):
    return n**2
result = [sqr(i) for i in x]
print(result)

print(list(map(sqr, x)))

def my_pow(i, power):
    return i**power
powers = [2, 3, 4, 5]
print(list(map(my_pow, x, powers)))
print(list(map(my_pow, x, powers[:3])))
print([my_pow(x[i], powers[i]) for i in range(len(powers))])
print([my_pow(x[i], powers[i]) for i in range(len(powers[:3]))])

from timeit import timeit
# help(timeit)
print(f'Time, seconds:  {timeit('[my_pow(x[i], powers[i]) for i in range(len(powers))]', number=10000, globals = {'x':x, 'powers':powers, 'my_pow':my_pow})}')
print(f'Time, seconds:  {timeit('list(map(my_pow, x, powers))', number=10000, globals = {'x':x, 'powers':powers, 'my_pow':my_pow})}')
print(f'Time, seconds:  {timeit('map(my_pow, x, powers)', number=10000, globals = {'x':x, 'powers':powers, 'my_pow':my_pow})}')

import sys
print(f'Size, bytes:  {sys.getsizeof([my_pow(x[i], powers[i]) for i in range(len(powers))])}')
print(f'Size, bytes:  {sys.getsizeof(list(map(my_pow, x, powers)))}')
print(f'Size, bytes:  {sys.getsizeof(map(my_pow, x, powers))}')

for e in map(my_pow, x, powers):
    print(e)

