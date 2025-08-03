# Скопіювати рішення для задачі 2,
# переробити таким чином, щоб для геттера, сеттера та делітера використовувалось одне і те ж ім“я.

class Car:
    def __init__(self, brand, model, distance, price):
        self.brand = brand
        self.model = model
        self.distance = distance
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @price.deleter
    def price(self):
        self.__price = 0

car1 = Car('Audi', 'A4', 50000, 10000)

print(car1.price)
car1.price = 20000
print(car1.price)
del car1.price
print(car1.price)