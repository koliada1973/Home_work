print('Task 1:')
# Генеруємо випадкове число від 1 до 10 включно
# Отримуємо від користувача варіант числа
# Далі в циклі:
    # Перевіряємо якщо вони не співпадають - пропонуємо ввести новий варіант
# Якщо відповідь правильна - друкуємо повідомлення

import random

num = random.randint(1, 10)  
user = int(input('Вгадайте число від 1 до 10! Ваш варіант : '))

while  user != num:
    user = int(input('Ви не вгадали! Спробуйте ще варіант : '))
print(f'Ви вгадали! Правильна відповідь - {num}')

