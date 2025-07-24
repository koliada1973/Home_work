# Task 1:
# Створіть клас з іменем Person.
# Зробіть так, щоб метод __init__() отримував ім'я, прізвище та вік як параметри і додавав їх як атрибути.
# Створіть ще один метод з назвою talk(), який виводить на екран привітання від особи,
# наприклад, такого змісту "Привіт, мене звати Карл Джонсон і мені 26 років".

class Person:
    def __init__(self, name, last_name,age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def talk(self):
        print(f"Привіт, мене звати {self.name} {self.last_name} і мені {self.age} років")

x_man = Person("Фрідріх", "Ніцше", 180)
x_man.talk()