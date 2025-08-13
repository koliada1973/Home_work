def MySquaresGenerator(_from, _to, step = 1):
    for i in range(_from, _to, step):
        yield i ** 2

c = MySquaresGenerator(1, 10,2)
for i in c:
    print(i)