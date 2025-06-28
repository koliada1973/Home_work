def func1(*args):
    return args

def func2(**kwargs):
    return kwargs

def func3(*args, **kwargs):
    return [args, kwargs]

print(func1(1, 2, 3, 4, 5))
print(func2(a=1, b=2, c=3))
print(func3(1, 2, 3, 4, 5, a=1, b=2, c=3))