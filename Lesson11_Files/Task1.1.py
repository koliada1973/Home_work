# Task1 (частина 1) - створення нового вихідного файлу з назвою myfile.txt
# і запис у нього рядка "Hello file world!":

with open('myfile.txt', 'w') as f:
    f.write('Hello file world!\n')

# Запустіть обидва скрипти із системного командного рядка.
# Чи з'явився новий файл у каталозі, де ви запускали скрипти?
#   Так, новий файл з'являється у каталозі, де запущено скрипт.

# Що, якщо ви додасте інший шлях до каталогу до імені файлу, який потрібно відкрити?
#   Якщо інший шлях не веде до цього файлу, то відкриття не відбувається.
#   Натомість виникає помилка, наприклад:
#   python: can't open file 'C:\\Users\\Admin\\OneDrive\\Desktop\\HomeWork\\Lesson9_modules_':
#   [Errno 2] No such file or directory
#   The system cannot find the path specified.