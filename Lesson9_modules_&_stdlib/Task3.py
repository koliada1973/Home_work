# Task 3:
# Функція для підрахунку кількості рядків у файлі
# Приймає або файл як об'єкт, або строку з назвою файлу
def count_lines(my_file):
    count_lines = 0
    if type(my_file) is str:    # Якщо отримано строку з назвою файлу
        with open(my_file) as file1:
            count_lines = len(file1.readlines())
    else:   # Якщо отримано файл як об'єкт
        count_lines = len(my_file.readlines())
    return count_lines

# Функція для підрахунку кількості символів у файлі
# Приймає або файл як об'єкт, або строку з назвою файлу
def count_chars(my_file):
    count_chars = 0
    if type(my_file) is str:    # Якщо отримано строку з назвою файлу
        with open(my_file) as file1:
            for line in file1:
                count_chars += len(line.strip())
    else:   # Якщо отримано файл як об'єкт
        for line in my_file:
            count_chars += len(line.strip())
    return count_chars

# Функція, що отримує назву файлу
# та викликає функції count_lines та count_chars
def test(filename):
    with open(filename) as my_file:
        print(f'Кількість рядків у файлі: {count_lines(my_file)}')
        my_file.seek(0)     # Повернення в начало файла
        print(f'Кількість символів у файлі: {count_chars(my_file)}')

if __name__ == '__main__':
    filename = input('Enter file name: ')
    # filename = 'C:\\Users\\Admin\\OneDrive\\Desktop\\HomeWork\\Lesson9_modules_&_stdlib\\state.txt'
    test(filename)


# Чи повинен ваш PYTHONPATH містити директорію, де ви створили mymod.py?
# - Імпорт у мене працює без додавання каталогу в sys.path

# У випадку виклику функції через консоль -
# доводиться передавати повний шлях до файлу

# У випадку запуску файлу напряму - достатньо вказати тільки назву_файлу.txt