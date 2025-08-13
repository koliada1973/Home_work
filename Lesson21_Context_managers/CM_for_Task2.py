import time
class File_context_manager:
    counter = 0
    def __init__(self, filename, mode = 'r', log_name = 'logfile.txt'):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.log_name = log_name
        self.log_file = None

    def __enter__(self):
        # Відкриття основного файлу:
        try:
            self.file = open(self.filename, self.mode, encoding='utf-8')
        except FileNotFoundError:
            with open(self.log_name, 'a', encoding='utf-8') as log_file:
                log_file.write(f"{time.strftime('%H:%M:%S')} Файл {self.filename} не знайдено!\n")
            raise
        else:
            with open(self.log_name, 'a', encoding='utf-8') as log_file:
                log_file.write(f"{time.strftime('%H:%M:%S')} Відкриття файлу {self.filename}\n")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file is not None:
            self.file.close()
        # Якщо помилка під час основного коду під контекстним менеджером:
        if exc_type:
            with open(self.log_name, 'a', encoding='utf-8') as log_file:
                log_file.write(f"{time.strftime('%H:%M:%S')} Під час виконання основного коду була виявлена помилка: {exc_type.__name__} [{exc_val}]!!!\n")
        with open(self.log_name, 'a', encoding='utf-8') as log_file:
            log_file.write(f"{time.strftime('%H:%M:%S')} Закриття файлу {self.filename}\n")
        return False