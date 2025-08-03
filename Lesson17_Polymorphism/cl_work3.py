# Створити клас Detail, з полями назва та вартість.
# Реалізувати додавання екземплярів класу Detail (по типу: detail_1 + detail_2) з допомогою __add__(), результат – сума вартостей товарів.
# Виконувати перевірку, щоб обидва доданки були типу Detail, в іншому випадку – видавати виключення TypeError.

class Detail:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return self.price + other.price
        else:
            raise TypeError("Об'єкти різного класу!")
        
detail1 = Detail("болт", 2.50)
detail2 = Detail("гайка", 3.50)

print(detail1 + detail2)