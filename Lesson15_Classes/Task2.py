# Task 2:
# Створити клас Dog з атрибутом класу 'age_factor' рівним 7.
# Створіть функцію __init__(), яка отримує значення віку собаки.
# Потім створіть метод `human_age`, який повертає вік собаки в людському еквіваленті.

class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * Dog.age_factor

Richard = Dog(4)
print(Richard.human_age())