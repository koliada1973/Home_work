# Task 1:
# Клас File Context Manager
# Створіть власний клас, який може поводитися як вбудована функція 'open'.
# Також потрібно розширити його функціональність лічильником та логуванням.
# Зверніть особливу увагу на реалізацію методу '__exit__',
# який повинен відповідати всім вимогам до контекстних менеджерів

import time
class File_context_manager:
    counter = 0
    def __init__(self, filename, mode = 'r', log_name = 'logfile.txt'):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.log_name = log_name
        # self.log_file = None
        self.__class__.counter += 1

    def __enter__(self):
        # Відкриття основного файлу:
        try:
            self.file = open(self.filename, self.mode, encoding='utf-8')
        except FileNotFoundError:
            with open(self.log_name, 'a', encoding='utf-8') as log_file:
                log_file.write(f"{time.strftime('%H:%M:%S')} [counter = {self.__class__.counter}] Файл {self.filename} не знайдено!\n")
            raise
        else:
            with open(self.log_name, 'a', encoding='utf-8') as log_file:
                log_file.write(f"{time.strftime('%H:%M:%S')} [counter = {self.__class__.counter}]  Відкриття файлу {self.filename}\n")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file is not None:
            self.file.close()
        # Якщо помилка під час основного коду під контекстним менеджером:
        if exc_type:
            with open(self.log_name, 'a', encoding='utf-8') as log_file:
                log_file.write(f"{time.strftime('%H:%M:%S')} [counter = {self.__class__.counter}]  Під час виконання основного коду була виявлена помилка: {exc_type.__name__} [{exc_val}]!!!\n")
        with open(self.log_name, 'a', encoding='utf-8') as log_file:
            log_file.write(f"{time.strftime('%H:%M:%S')} [counter = {self.__class__.counter}]  Закриття файлу {self.filename}\n")
        return False    # Повертаємо False, щоб підіймалась помилка в основному коді під менеджером.
                        # Якщо замінити на True - помилка не буде виходити назовні

# Використання:
with File_context_manager(filename = 'new_file.txt', mode = 'w') as f:
    f.write('Рядок тексту\n')

# Якщо виникає помилка в основному коді під контекстним менеджером -
# крім повідомлення про помилку, також робиться запис в лог-файл
with File_context_manager(filename = 'new_file.txt', mode = 'a') as f:
    f.write('Ще один рядок\n')
    # 1 / 0  # Помилка буде записана в лог-файл

# Переглянемо результат обох файлів
with open('new_file.txt', encoding='utf-8') as f:
    print('new_file.txt:')
    print(f.read())

with open('logfile.txt', encoding='utf-8') as f:
    print('logfile.txt:')
    print(f.read())