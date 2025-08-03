# Створити клас Person, в метод ініціалізації передається name.
#  Створити:
# ·      метод activity, в якому викликати raise NotImplementedError,
# ·      метод activity_and_title, який виводить разом:
# ◦  name екземпляру,
# ◦  результат метод activity.
# Від нього наслідувати:
# ·      клас BusinessAnalyst
# ·      клас Programmer
# ·      клас Tester
# В кожному з класів переозначити метод activity, повертати текст, відповідно:
# ·      « : пише текст »
# ·      « : пише код »
# ·      « : ловить баги»
# Створити список екземплярів (від кожного класу - екземпляр).
# В циклі запусити виклик методу activity_and_title().

class Person:
    def __init__(self, name):
        self.name = name

    def activity(self):
        raise NotImplementedError("Помилка!")

    def activity_and_title(self):
        print(self.name, self.activity())

class BusinessAnalyst(Person):
    def activity(self):
        return f" : пише текст"

class Programmer(Person):
    def activity(self):
        return f" : пише код "

class Tester(Person):
    def activity(self):
        return f" : ловить баги"

List_of_instances = [BusinessAnalyst("Іvan"), Programmer("Petro"), Tester("Mark")]
for e in List_of_instances:
    e.activity_and_title()

