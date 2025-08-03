# Task 1:
# Школа
# Створіть структуру класів у python, що представляє людей у школі.
# Створіть базовий клас з ім'ям Person, клас з ім'ям Student і ще один з ім'ям Teacher.
# Спробуйте знайти якомога більше методів та атрибутів, які належать до різних класів, і пам'ятайте, які з них є спільними, а які ні.
# Наприклад, ім'я має бути атрибутом Person, тоді як зарплата має бути доступною лише для вчителя.

class Person:
    def __init__(self, full_name, age, address, hobby):
        self.full_name = full_name
        self.age = age
        self.address = address
        self.hobby = hobby

    def change_age(self, new_age):
        self.age = new_age

    def change_address(self, new_address):
        self.address = new_address

    def change_hobby(self, new_hobby):
        self.hobby = new_hobby

class Student(Person):
    def __init__(self, full_name, age, address, hobby, faculty, course, group, average_grade):
        super().__init__(full_name=full_name, age=age, address=address, hobby=hobby)
        self.faculty = faculty
        self.course = course
        self.group = group
        self.average_grade = average_grade

    def change_course(self, new_course):
        self.course = new_course

    def change_average_grade(self, new_average_grade):
        self.average_grade = new_average_grade

    def print_info(self):
        print(f"""Інформація:           
    Повне ім'я: {self.full_name}
    Вік: {self.age} 
    Адреса: {self.address} 
    Хоббі: {self.hobby} 
    Факультет: {self.faculty} 
    Курс: {self.course} 
    Група: {self.group}
    Середній навчальний бал: {self.average_grade} \n""")

class Teacher(Person):
    def __init__(self, full_name, age, address, hobby, faculty, department, subject, title, salary):
        super().__init__(full_name=full_name, age=age, address=address, hobby=hobby)
        self.faculty = faculty
        self.department = department
        self.subject = subject
        self.title = title
        self.salary = salary

    def change_department(self, new_department):
        self.department = new_department

    def change_salary(self, new_salary):
        self.salary = new_salary

    def change_title(self, new_title):
        self.title = new_title

    def print_info(self):
        print(f"""Інформація:           
    Повне ім'я: {self.full_name}
    Вік: {self.age} 
    Адреса: {self.address} 
    Хоббі: {self.hobby} 
    Факультет: {self.faculty} 
    Кафедра: {self.department} 
    Звання: {self.title} 
    Зарплатня: {self.salary} \n""")

st1 = Student('Іванов Олег Петрович', 21, 'с.Червоне дишло, вул.Крайня 1', 'риболовля', 'агрономія', 2, 'Агро2025', 9)
teach1 = Teacher('Тарасов Віктор Петрович', 78, 'Маріуполь, проспект Миру, 106', 'шахи, біг','металургія чорних металів', 'кафедра металургії чавуну', 'доменний процес', 'професор', 20000)

print(st1.full_name)
print(teach1.full_name)

st1.print_info()
teach1.print_info()

teach1.change_salary(25000)
teach1.print_info()