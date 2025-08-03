# Задача 2. -
# Створіть класи Class_1, Class_4, Class_7 з одним методом display_class(),
# що виводить ім“я цього класу (наприклад, для Class_1: print(‘Class_1’),
# не потрібно використовувати self.__class__.__name__).
# ·      Нехай клас Class_2 наслідується від класу Class_1.
# ·      Клас 3 – від 4.
# ·      Клас 5 – від 6 , а той в свою чергу – від 7 (в цей клас додайте ще метод display(), що виводить „I’m from Class_7“).
# ·      Клас 8 наслідується від класів 2, 3, 6.
# 1      Створіть екземпляр класу 8, запустіть його метод display_class(), чи коректно відпрацював ?
# 2      Поміняйте порядок наслідування класу 8 на 6, 2, 3 , що змінилось.
# 3      Викличте метод display(), відпрацював ? Зрозуміло чому ?
# 4      Який метод виводить порядок виконання класів ? (Не було в матеріалах уроку ? А загуглити ? ;) )

class Class_1:
    def display_class(self):
        print('Class_1')

class Class_4:
    def display_class(self):
        print('Class_4')

class Class_7:
    def display_class(self):
        print('Class_7')

class Class_6(Class_7):
    # def display_class(self):
    #     print('Class_6')
    pass

class Class_2(Class_1):
    # def display_class(self):
    #     print('Class_2')
    pass

class Class_3(Class_4):
    # def display_class(self):
    #     print('Class_4')
    pass

class Class_5(Class_2, Class_3, Class_6):
    # def display_class(self):
    #     print('Class_5')
    pass

class Class_6(Class_7):
    def display(self):
        print("I’m from Class_7")
    pass

class Class_8(Class_6, Class_2, Class_3):
    # def display_class(self):
    #     print('Class_8')
    pass

c8 = Class_8()

c8.display_class()
c8.display()

print(Class_8.mro())
print(Class_8.__mro__)
print(c8.__class__.mro())
print(type(c8).mro())