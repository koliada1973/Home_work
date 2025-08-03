# Task 4:
# Користувацький виняток
# Створіть свій користувацький виняток з назвою "CustomException",
# який можна успадкувати від базового класу Exception,
# але розширити його функціональність,
# щоб кожне повідомлення про помилку записувалося до файлу з назвою "logs.txt".
# Поради: Використовуйте метод __init__ для розширення функціональності збереження повідомлень у файл

from datetime import datetime   # Для додавання часу до повідомлення про помилку

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__()
        self.log_file_name = 'my_log_file.txt'
        self.time_string = f"[{datetime.now().hour:02d}:{datetime.now().minute:02d}:{datetime.now().second:02d}]"
        self.message = f"{self.time_string}: {msg} (CustomException)"
        self.log_file()

    def log_file(self):
        with open(self.log_file_name, 'a', encoding="utf-8") as f:
            f.write(f"{self.message}\n")

raise CustomException("Сталася критична помилка!")
