def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)




while True:
    N = input('Введіть ціле число від 0 до 30: ')
    if N.isalpha():
        print('Помилка вводу!')
        continue
    elif int(N) < 0 or int(N) > 30:
        print('Помилка вводу!')
        continue
    else:
        print(fibonacci(int(N)))