# Завдання
# Створи абстрактний клас Vehicle з:
# приватним атрибутом __speed
# конструктором, що приймає швидкість
# абстрактним методом move()
# dunder методом __lt__ для порівняння швидкості двох транспортних засобів
# Створи два підкласи Car і Bike, які:
# наслідують Vehicle
# реалізують метод move(), який виводить:
# "Car їде зі швидкістю <speed> км/год"
# "Bike їде зі швидкістю <speed> км/год" відповідно
# Створи список з кількох об’єктів Car і Bike з різною швидкістю.
# Відсортуй список за швидкістю, використовуючи sorted() та __lt__.
# Виведи інформацію про кожен транспортний засіб, викликаючи метод move().

class Vehicle:
    def __init__(self, speed):
        self.__speed = speed

    def move(self):
        raise NotImplementedError

    def __lt__(self, other):
        return self.__speed < other.__speed

    def __repr__(self):
        return f"Vehicle ({self.__speed})"

class Car(Vehicle):
    def move(self):
        print(f"Car їде зі швидкістю {self._Vehicle__speed} км/год")

class Bike(Vehicle):
    def move(self):
        print(f"Bike їде зі швидкістю {self._Vehicle__speed} км/год")

vehicle_list = [Car(100), Car(120), Bike(110), Bike(140)]
# for i in vehicle_list:
#     i.move()

sorted_list = sorted(vehicle_list)
for i in sorted_list:
    i.move()

print(vehicle_list)
# for i in vehicle_list.sort():
#     i.move()