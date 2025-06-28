def to_power(x: int | float, exp: int) -> int | float:
    if exp <= 0:
        return 'This function works only with exp > 0'
    if exp == 1:
        return x
    else:
        return x * to_power(x, exp - 1)

print(to_power(2, 3))
print(to_power(3.5, 2))
print(to_power(2, -1))