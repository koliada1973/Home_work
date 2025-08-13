# Task 2:
# Напишіть тести для додатку Phonebook, який ви реалізували в модулі 1.
# Спроектувати тести для цього рішення та написати тести з використанням бібліотеки unittest

import unittest
from unittest.mock import patch
import phone_book

class Phone_book_Test(unittest.TestCase):
    def setUp(self):
        self.contact = {
    "0": {
        "phone_number": "123",
        "first_name": "Іван",
        "last_name": "Сідоров",
        "full_name": "Іван Сідоров",
        "state": "Україна",
        "city": "Харків"
    }
}

    # Функція phone_book_update робить декілька викликів input(),
    # тому використовуємо side_effect щоб передати список значень, які input() повертатиме послідовно (Chat GPT):
    @patch('builtins.input', side_effect=["123", 'Петро', "Сідоров", "Україна", "Харків"])
    def test_phone_book_update(self, mock_input):
        updated_contact = phone_book.phone_book_update(self.contact)

        expected_contact = {
    "0": {
        "phone_number": "123",
        "first_name": "Петро",
        "last_name": "Сідоров",
        "full_name": "Петро Сідоров",
        "state": "Україна",
        "city": "Харків"
    }
}

        self.assertEqual(updated_contact, expected_contact)

if __name__ == '__main__':
    unittest.main()