import random

def r1():
    return random.randint(0, 10)
def r2():
    return random.randint(0, 100)
def r3():
    return random.randint(0, 300)
def main(*args):
    even_funcs = [f() for f in args if f() % 2 == 0]
    return even_funcs

print(main(r1, r2, r3))

