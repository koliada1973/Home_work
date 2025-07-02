class ABC:
    def __init__(self, a):
        self.a = a
    def __call__(self, b):
        return self.a + b

K = ABC(15)
L = ABC(15)
print(L(5), id(L), type(L))
print(L(3), id(L), type(L))
print(L.a)