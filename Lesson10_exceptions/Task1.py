# Task 1:
# Напишіть функцію з викликом oops, яка явно згенерує виключення IndexError при виклику.
# Потім напишіть іншу функцію, яка викликає oops всередині оператора try/except, щоб перехопити помилку.
# Що станеться, якщо змінити функцію oops так, щоб вона генерувала виключення KeyError замість IndexError?

def oops_function():
    raise IndexError('Oops function IndexError')
    # raise KeyError('Oops function IndexError')

def another_function():
    try:
        oops_function()
    except IndexError:
        print('IndexError')

another_function()
# При виклику oops_function оператор except перехоплює помилку і виконує друк повідомлення 'IndexError'
# Але, якщо змінити oops_function так, щоб raise генерувала KeyError, то except не перехоплює цю помилку ...
# що веде до зупинки з помилкою KeyError: 'Oops function IndexError'
