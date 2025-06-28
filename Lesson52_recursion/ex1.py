# Рекурсивне обертання числа (задача з Codewars)
n = 1234
s = 0
def my_function(n):
    global s
    x = n % 10
    if n // 10 == 0:
        return x
    else:
        s += 1
        result = (x * (10**s)) + my_function(n // 10)
    return result

print(my_function(n))

