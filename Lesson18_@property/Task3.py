# Task 3:
# Напишіть клас TypeDecorators, який має декілька методів для перетворення результатів функцій до заданого типу (якщо це можливо):
# методи: to_int to_str to_bool to_float
from functools import wraps

class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(string):
            try:
                string = int(string)
            except ValueError:
                print(f"Рядок '{string}' неможливо перетворити на int")
            else:
                return func(string)
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(string):
            try:
                string = float(string)
            except ValueError:
                print(f"Рядок '{string}' неможливо перетворити на float")
            else:
                return func(string)
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(string):
            try:
                string = str(string)
            except ValueError:
                print(f"Рядок '{string}' неможливо перетворити на str")
            else:
                return func(string)
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(string):
            try:
                string = bool(string)
            except ValueError:
                print(f"Рядок '{string}' неможливо перетворити на bool")
            else:
                return func(string)
        return wrapper

@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string

print(do_nothing('25') == 25)
print(do_something('True') is True )

