def f_sqr(a):
    return a ** 2

def f_ext(b):
    def f_int(c):
        return b(c)
    return f_int

f = f_ext(f_sqr)

print(f(10))