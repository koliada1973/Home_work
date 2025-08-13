class My_context_manager:
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.gile_mode = file_mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.gile_mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file is not None:
            self.file.close()
        if exc_type:
            print(f'Помилка:exc_type = {exc_type} exc_val = {exc_val} exc_tb = {exc_tb}')
        return True

with My_context_manager('test.txt', 'w') as f:
    f.write('Hello')
    1 + '1'
    1 / 0


from contextlib import contextmanager
@contextmanager
def my_context_manager(file_name, file_mode):
    file = open(file_name, file_mode)
    yield file
    file.close()

with my_context_manager('test.txt', 'w') as f:
    f.write('By-by...')
    1 + '1'
    1 / 0


