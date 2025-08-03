# Створити клас Авто, приймає атрибути:
# ·      Марка авто
# ·      Модель авто
# ·      Пробіг
# ·      Вартість (приватний атрибут)
# Реалізувати методи (для атрибуту „вартість“) через синтаксис (my_property = property(getx, setx, delx, "I'm the 'x' property.")
# ·      Створити екземпляр класу,
# ·      відпрацювати всі методи,
# ·      викликати стрічку документації.

class Car:
    def __init__(self, brand, model, distance, price):
        self.brand = brand
        self.model = model
        self.distance = distance
        self.__price = price

    def getx(self):
        return self.__price

    def setx(self, new_price):
        self.__price = new_price

    def delx(self):
        self.__price = 0

    my_property = property(getx, setx, delx, "I'm the 'x' property.")

car1 = Car('Audi', 'A4', 50000, 10000)

print(car1.my_property)
car1.my_property = 20000
print(car1.my_property)
del car1.my_property
print(car1.my_property)