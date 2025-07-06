# Напишіть декоратор arg_rules, який перевіряє аргументи, що передаються у функцію.
# Декоратор повинен приймати 3 аргументи:
# - max_length: 15
# - type_: str
# - contains: [] - список символів, які повинен містити аргумент
# Якщо якась з перевірок правил повертає False, функція повинна повернути False і вивести причину невдачі;
# в іншому випадку, повернути результат.

from functools import wraps

def arg_rules(type_: type, max_length: int, contains: list):
    def my_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if type(args[0]) != type_:
                print(f'Неправильний тип аргументу! Має бути {type_}')
                return False
            elif max_length < len(args[0]):
                print(f'Довжина аргументу більше {max_length} символів!')
                return False
            elif all(c in args[0] for c in contains) == False:  # Перевірка чи містить аргумент потрібні символи (компрехеншн з all)
                print(f'Аргумент має містити наступні символи: {contains}')
                return False
            else:
                result = function(*args, **kwargs)
                return result
        return wrapper
    return my_decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False                            # Має викликати помилку довжини рядка
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'   # Має працювати без помилки


# Виклики функції з різними аргументами (для наочності, це не потрібно за умовами задачі!!!)
create_slogan('Саша')
create_slogan(['S@SH05'])
print(create_slogan('S@SH05'))  # Правильний варіант