# Task 3:

# Функція, що проводить арифметичні операції з довільним числом аргументів.
# Якщо перший аргумент (операнд) не є арифметичним: '/', '*', '+' або '-' - повертається повідомлення про помилку.
# Також аргументи, що не є int або float - ігноруються.
def make_operation(operand, *args):
    if operand not in '/*+-':
        result = 'Ви ввели некоректний символ операції: ' + operand
    else:
        # Щоб виключити віднімання числа від самого себе -
        # присвоюємо результату значення першого числа (другого аргумента функції):
        result = args[0]
        if operand == '+':
            for arg in args[1:]:
                if type(arg) == int or type(arg) == float:
                    result += arg
        elif operand == '-':
            for arg in args[1:]:
                if type(arg) == int or type(arg) == float:
                    result -= arg
        elif operand == '*':
            for arg in args[1:]:
                if type(arg) == int or type(arg) == float:
                    result *= arg
        elif operand == '/':
            for arg in args[1:]:
                if type(arg) == int or type(arg) == float:
                    result /= arg
    return result

print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))