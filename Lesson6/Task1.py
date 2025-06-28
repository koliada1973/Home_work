# Task 1:

# Імпортуємо модуль random
# Створюємо пустий список my_list
#
# В циклі while (поки кількість елементів списку my_list меньше 10):
#   генеруємо випадкове число та заносимо його в хвіст списку my_list,
# далі через функцію max() находимо максимальне значення і друкуємо.

import random

my_list = []

while len(my_list) < 10:
    my_list.append(random.randint(1, 100))

print('Task 1:')
print(f'Список десяти випадкових чисел: {my_list}')
print(f'Найбільше число:  {max(my_list)}')
