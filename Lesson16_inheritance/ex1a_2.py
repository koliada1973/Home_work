#  Розказати коротко про другий варіант ініціалізації
#        super().__init__(arg1, arg2)
#        Class_2.__init__(self, arg3, arg4)
#
# Створіть базовий клас Person, у якого є:
#    метод __init__, що приймає ім'я та вік людини. Їх необхідно зберегти в атрибути name і age відповідно
#    метод display_person_info , який друкує інформацію в такому вигляді:
#    Person: {name}, {age}
# Потім створіть клас Company , у якого є:
#    метод __init__, що приймає назву компанії та місто її заснування. Їх необхідно зберегти в атрибути екземпляра company_name і location відповідно
#    метод display_company_info , який друкує інформацію в такому вигляді:
#    Company: {company_name}, {location}
# І наприкінці створіть клас Employee , який:
#    успадкований від класів Person і Company
#    має метод __init__, що приймає назву ім'я людини, її вік, назву компанії та місто заснування. Необхідно делегувати створення атрибутів name і age класу Person , а атрибути company_name і location має створити клас Company
# Після множинного успадкування у екземплярів класу Employee будуть доступні методи батьківських класів. Перевірте це.

class Person:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        super().__init__(**kwargs)

    def display_person_info(self):
        print(f"Person: {self.name}, {self.age}")

class Company:
    def __init__(self, company_name , location, since, **kwargs):
        self.company_name  = company_name
        self.location = location
        self.since = since
        super().__init__(**kwargs)

    def display_company_info(self):
        print(f"Company: {self.company_name}, {self.location}, {self.since}")

class Employee(Company, Person):
    def __init__(self, name, age, company_name , location, since):
        super().__init__(name=name, age=age, company_name=company_name , location=location, since=since)
        # Person.__init__(self, name, age)
        # Company.__init__(self, company_name, location, since)


person1 = Employee("Sergey Brin", "51", "Google", "Mountain View, California, U.S", 1998)
person1.display_company_info()
person1.display_person_info()



