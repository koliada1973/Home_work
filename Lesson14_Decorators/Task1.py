# Напишіть декоратор, який виводить функцію з переданими їй аргументами.
# УВАГА! Він повинен виводити функцію, а не результат її виконання!
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_args = [str(a) for a in args]      # Отримуємо список позиційних аргументів
        func_args = ", ".join(func_args)        # Складаємо в рядок для приведення до вигляду, заданого в задачі..
        func_kwargs = [k for k in kwargs]       # Отримуємо список іменованих аргументів
        func_kwargs = ", ".join(func_kwargs)    # Складаємо в рядок для приведення до вигляду, заданого в задачі..
        if func_args != '' and func_kwargs != '':
            print(f'Функція {func.__name__} викликана з позиційними аргументами: {func_args}, та з іменованими аргументами: {func_kwargs}.')
        elif func_args != '' and func_kwargs == '':
            print(f'Функція {func.__name__} викликана з позиційними аргументами: {func_args}.')
        elif func_args == '' and func_kwargs != '':
            print(f'Функція {func.__name__} викликана з іменованими аргументами: {func_kwargs}.')
        elif func_args == '' and func_kwargs == '':
            print(f'Функція {func.__name__} викликана без аргументів.')
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

# Виклики функцій з різним складом аргументів:
add(1, 4)
square_all(1, 2, 3, x = 4, y = 5)
square_all(s = 4, t = 10)
square_all()
