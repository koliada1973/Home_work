def factorial(n):
    x = 0   # створювати змінну необовязково, можно просто повертати return n * factorial(n - 1) після else
    if n ==0 or n == 1:
        return 1
    else:
        x = n * factorial(n - 1)
        return x

print(factorial(5))