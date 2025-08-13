# Task 2:
# Написання тестів для контекстного менеджера
# Візьміть вашу реалізацію класу контекстного менеджера із завдання 1 і напишіть для неї тести.
# Намагайтеся охопити якомога більше варіантів використання, позитивних, коли файл існує і все працює, як задумано.
# А також напишіть тести, коли ваш клас видає помилки або у вас виникають помилки в контекстному наборі під час виконання.

import unittest
from CM_for_Task2 import File_context_manager

class Test_File_context_canager(unittest.TestCase):
    # Використання файлового контекстного менеджера і в кінці перевіряємо чи закрився файл:
    def test_file_closed(self):
        with File_context_manager('test.txt', 'w') as f:
            f.write('test \n')
        self.assertTrue(f.closed)

    # Випадок, коли файл не існує:
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            with File_context_manager('test2.txt') as f:
               pass

    # Передача помилки
    def test_error(self):
        with self.assertRaises(ValueError):
            with File_context_manager('test.txt') as f:
                raise ValueError('test ValueError!')

if __name__ == "__main__":
    unittest.main()