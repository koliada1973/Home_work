def new_decorator(func):
    def wrapper(*args, **kwargs):
        print('Виконання коду в декораторі до виконання переданої функції...')
        func(*args, **kwargs)
        print('Виконання коду в декораторі після виконання переданої функції...\n')
    return wrapper

def function1():
    print("Функція1, що декорується...")

x = new_decorator(function1)
x()


@new_decorator
def function2():
    print("Функція2, що декорується...")
function2()

print(f"Ім'я функції x:  ",x.__name__)           # wrapper, тобто повертається ім'я не декоруємої функції,
print(f"Ім'я функції function2:  ",function2.__name__)   # а функції wrapper, що оголошена всередині декоратора..
print('\n\n')



from functools import wraps

def new_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Виконання коду в декораторі до виконання переданої функції3...')
        func(*args, **kwargs)
        print('Виконання коду в декораторі після виконання переданої функції3...\n')
    return wrapper

@new_decorator
def function3():
    print("Функція3, що декорується...")
function3()

print(f"Ім'я функції function3 з використанням модуля functools.wraps:  ", function3.__name__)
