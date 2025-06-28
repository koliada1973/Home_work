# Task_1:

# Отримуємо від користувача речення (рядок)
# Розбираємо окремі слова (майбутні keys) за допомогою метода split() в список string_parts
# Створюємо пустий словник my_dict
# В циклі перевіряємо кожен елемент списку string_parts чи є він як ключ в словнику my_dict:
#     якщо немає - додаємо його в словник my_dict як ключ і кількість входжень як значення
# Друкуємо my_dict

string_parts = input("Task 1:\nВведіть речення: ").split()
my_dict = {}

for key in string_parts:
    if key not in my_dict:
        my_dict[key] = string_parts.count(key)

print(f'Словник: {my_dict}')