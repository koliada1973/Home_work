User_number = input('Integer pls: ')
i = int(User_number)

for j in range(1, i + 1):
    is_prime = True  # Assume j is prime
    if j < 2:  # Numbers less than 2 are not prime
        is_prime = False
    else:
        for divider in range(2, int(j ** 0.5) + 1):  # Check divisibility up to the square root
            if j % divider == 0:
                is_prime = False
                break

    if is_prime:
        print('|', '.' * (j - 1), '*', '.' * (i - j), sep='', end=f'|{j}\n')
    else:
        print('|', '.' * i, sep='', end='|\n')