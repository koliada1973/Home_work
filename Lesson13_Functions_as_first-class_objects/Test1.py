def add_five(x):
    return x + 5

def do_twice(f):
    def resulting_func(x):
        return f(f(f(x)))
    return resulting_func

result = do_twice(add_five)
print(result(7))

import math

def cilinder_volume_function(r):
    def volume(h):
        return math.pi * r ** 2 * h
    return volume
volume_of_r10 = cilinder_volume_function(10)
print(volume_of_r10(30))
print(cilinder_volume_function(10)(30))