def mult(a: int, n: int):
    if a < 0 or n < 0:
        return "This function works only with postive integers"
    if n == 0:
        return 0
    else:
        return a + mult(a, n - 1)

print(mult(2, 4) == 8)
print(mult(2, 0) == 0)
print(mult(2, -4))