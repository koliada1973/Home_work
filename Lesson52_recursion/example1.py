def print_to(n):
    if n >= 1:
        print_to(n-1)
        print(n)
print_to(9)