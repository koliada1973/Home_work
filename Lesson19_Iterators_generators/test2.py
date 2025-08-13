class MySquareIterator:
    def __init__(self, _from, _to, step=1):
        self.index = _from
        self.to = _to
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.to:
            raise StopIteration
        else:
            val = self.index ** 2
            self.index += self.step
            return val

c = MySquareIterator(1, 10, 2)
for i in c:
    print(i)
