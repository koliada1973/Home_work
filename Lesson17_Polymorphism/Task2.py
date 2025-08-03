# Task 2:
# Бібліотека
# Напишіть структуру класу, яка реалізує бібліотеку.
# Класи:
# 1) Бібліотека - ім'я, книги = [], автори = []
# 2) Книга - ім'я, рік, автор (автор повинен бути екземпляром класу Author)
# 3) Автор - ім'я, країна, день народження, книги = []
# Клас бібліотеки
# Методи:
# - new_book(ім'я: str, рік: int, автор: Author) - повертає екземпляр класу Book і додає книгу до списку книг для поточної бібліотеки.
# - group_by_author(author: Author) - повертає список всіх книг, згрупованих за вказаним автором
# - group_by_year(year: int) - повертає список всіх книг, згрупованих за вказаним роком
# Всі 3 класи повинні мати читабельні методи __repr__ та __str__.
# Крім того, клас book повинен мати змінну класу, яка містить кількість усіх наявних книг

class Author:
    def __init__(self, author_name:str, author_country:str, author_birthday:str):
        self.author_name = author_name
        self.author_country = author_country
        self.author_birthday = author_birthday
        self.author_books_list = []

    def __str__(self):
        return f"__str__: Автор {self.author_name}, дата народження: {self.author_birthday} ({self.author_country})"

    def __repr__(self):
        return self.__str__()

class Book:
    amount = 0
    def __init__(self, book_name:str, book_year:int):
        self.book_name = book_name
        self.book_year = book_year
        self.book_author = None
        Book.amount += 1

    def __str__(self):
        return f"__str__: Книга \"{self.book_name}\", рік видання: {self.book_year} (автор: {self.book_author.author_name})"

    def __repr__(self):
        return self.__str__()

class Library:
    def __init__(self, lib_name:str):
        self.lib_name = lib_name
        self.lib_books = []

    def new_book(self, book_name:str, book_year:int, book_author: Author):
        new_book = Book(book_name, book_year)
        new_book.book_author = book_author
        book_author.author_books_list.append(new_book)
        self.lib_books.append(new_book)
        return new_book

    def group_by_author(self, author: Author):
        return [book for book in self.lib_books if book.book_author == author]

    def group_by_year(self, year: int):
        return [b for b in self.lib_books if b.book_year == year]

    def __str__(self):
        return f"__str__: Бібліотека: \"{self.lib_name}\""

    def __repr__(self):
        return self.__str__()

# Створюємо екземпляр бібліотеки:
lib1 = Library("Полтавська обласна бібліотека для юнацтва імені Олеся Гончара")

# Створюємо екземпляри авторів:
author1 = Author('Джордж Оруелл', 'Велика Британія', '25 липня 1903')
author2 = Author('Марі Кореллі', 'Сполучене Королівство Великої Британії та Ірландії', '1 травня 1855')
author3 = Author('Люсі Мод Монтгомері', 'Канада', '30 листопада 1874')

# Створюємо екземпляри книг:
book1 = lib1.new_book('1984', 1948, author1)
book2 = lib1.new_book('Скотний двір', 1945, author1)
book3 = lib1.new_book('Спокута сатани', 1895, author2)
book4 = lib1.new_book('Енн із Зелених дахів', 1908, author3)


# Друк інформації про всі наявні в бібліотеці книги:
for b in lib1.lib_books:
    print(f"Назва книги: \"{b.book_name}\"")
    print(f"Рік виходу книги: {b.book_year}")
    print(f"Автор: {b.book_author.author_name}")
    print(f"День народження автора: {b.book_author.author_birthday}")
    print(f"Країна автора: {b.book_author.author_country}\n")

# Друк змінної класу Book, яка містить кількість усіх наявних книг
print(f"Загальна кількість книг в бібліотеці: {Book.amount}\n")

# Друк списку книг, згрупованих за автором
print("список всіх книг, згрупованих за вказаним автором:")
book_list = lib1.group_by_author(author3)
for b in book_list:
    print(f"{b.book_author.author_name}: \"{b.book_name}\" ({b.book_year})")

# Друк списку книг, згрупованих за роком видання
print("\nсписок всіх книг, згрупованих за вказаним роком:")
book_list = lib1.group_by_year(1895)
for b in book_list:
    print(f"{b.book_author.author_name}: \"{b.book_name}\" ({b.book_year})")

# Друк __str__, __repr__ для екземплярів бібліотеки, книги, автора:
print()
print(lib1.__str__())
print(book3.__repr__())
print(author2.__repr__())