x = [1, 2, 0, 34, -6, 7, 8, 2, 2, 1, 4, 6, 7]
result = []
for i in x:
    if i > 2:
        result.append(i)
print(result)

result = [i for i in x if i > 2]
print(result)

print(list(filter(lambda i: i > 2, x)))

print(list(filter(None, x)))

from timeit import timeit
print(f'Time, seconds:  {timeit('list(filter(lambda i: i > 2, x))', number=100000, globals={'x':x})}')
print(f'Time, seconds:  {timeit('[i for i in x if i > 2]', number=10000, globals={'x':x})}')

a = [4, 56, 2, -5, 7]
b = ['a', 'b', 'c', 'd', 'e']
print([(b[i], a[i]) for i in range(len(a))])
print(list(zip(b, a, [78, 56, 45, 89, 65])))
print(f'Time, seconds:  {timeit('list(zip(b, a))', number=10000, globals=dict(a=a, b=b))}')
print(f'Time, seconds:  {timeit('[(b[i], a[i]) for i in range(len(a))]', number=10000, globals=dict(a=a, b=b))}')

from itertools import zip_longest
print(list(zip_longest([1, 2, 3], [45, 65, 25, 35, 34, 78, 12])))
print(list(zip_longest([1, 2, 3], [45, 65, 25, 35, 34, 78, 12], fillvalue='111')))


