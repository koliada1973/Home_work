# Напишіть програму на Python для доступу до функції всередині функції
# (Поради: використовуйте функцію, яка повертає іншу функцію)

# Якась функція для прикладу:
def revers_str(string):
    if len(string) == 1:
        return string[0].upper() if string[0] not in " '…-,—.?!" else ""
    else:
        s = string[0].upper() if string[0] not in " '…-,—.?!" else ""
        return revers_str(string[1:]) + s

# Функція з функцією всередині, що повертає іншу функцію:
def my_func(func):
    def func2(a):
        return func(a)
    return func2

# Змінна f, в яку передаємо функцію my_func, яка в свою чергу отримує функцію revers_str як аргумент:
f = my_func(revers_str)

text = """
        Випив...
        Вижив!
        Її
        вижив.
        Випив!"""

print(f(text))