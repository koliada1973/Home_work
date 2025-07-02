def my_sum(*args):
    s = args[0]
    for a in args[1:]:
        s += a
    return s
def my_mult(*args):
    m = args[0]
    for a in args[1:]:
        m *= a
    return m
def my_div(*args):
    div = args[0]
    for a in args[1:]:
        div /= a
    return div
def my_minus(*args):
    minus = args[0]
    for a in args[1:]:
        minus -= a
    return minus

operations = {
    '*': my_mult,
    '/': my_div,
    '-': my_minus,
    '+': my_sum,
}

def calc(operator, *args):
    if operator in operations:
        my_func = operations.get(operator)
        return my_func(*args)

print(calc('+', 10, 2, 4))