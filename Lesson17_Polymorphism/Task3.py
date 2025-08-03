# Task 3:
# Fraction
# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *)
# з належною перевіркою й обробкою помилок.
# Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction

class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def reduction_of_fractions(self, other):
        """Метод, що виконує скорочення дробів"""
        a1 = int(self.a)
        a2 = int(other.a)
        b1 = int(self.b)
        b2 = int(other.b)
        list1 = [a1, a2, b1, b2]
        # Складаємо список спільних дільників
        list2 = []
        # В циклі перебираємо по черзі всі числа від 1 до найбільшого числа з чотирьох чисел дробів:
        # якщо всі чотири числа діляться на число, то це число записуємо в список спільних дільників
        for i in range(max(list1)):
            OK = True
            # Намагаємось поділити по черзі кожного з чотирьох числа дробів на вибране число
            for j in list1:
                x = 0
                try:
                    x = j % i
                except ZeroDivisionError:
                    OK = False
                    continue
                if x != 0:
                    OK = False
                    continue
            # Якщо всі числа в списку поділились без залишку на вибране число - заносимо його в список спільних дільників
            list2.append(i) if OK else None
        # Вибираємо наібільший спільний дільник зі списку спільних дільників
        NSK = max(list2)
        # Скорочуємо дробі, поділивши кожне значення на найбільший спільний дільник
        if NSK != 0:
            self.a = int(self.a / NSK)
            self.b = int(self.b / NSK)
            other.a = int(other.a / NSK)
            other.b = int(other.b / NSK)

    def special_method(self, other, operation:str):
        """Метод, що виконує наступні дії:
            - за допомогою алгоритму Евкліда розраховує наіменьший спільний дільник;
            - знаходить наіменьше спільне кратне знаменників дробів;
            - приводить дробі до спільного дільника;
            - реалізує потрібну операцію з дробами;
            - та виконує скорочення дробі."""
        a1 = self.a     # Створюємо тимчасові змінні для збереження числівників та знаменників дробів наших екземплярів
        a2 = self.b     # (значення в самих екземплярах ще будуть потрібні в подальшому)
        b1 = other.a
        b2 = other.b
        # Знаходимо найбільший спільний дільник (НСД) знаменників дробів (a і b) за допомогою алгоритму Евкліда
        # (він базується на повторюваному діленні з остачею до тих пір, поки остача не стане рівною нулю.
        # Останній ненульовий залишок і є НСД):
        try:
            while b2 != 0:
                a2, b2 = b2, a2 % b2
            NSD = a2
            # Знаходимо наіменьше спільне кратне (НСК) знаменників дробів (a і b):
            NSK = int((self.b * other.b) / NSD)
            # Приводимо дробі до спільного дільника:
            self.a = int(self.a * (NSK / self.b))
            other.a = int(other.a * (NSK / other.b))
            self.b = other.b = NSK
        except TypeError:
            print("TypeError (NOD)!")
        except ZeroDivisionError:
            print("ZeroDivisionError (NOD)!")
        # Виконуємо задану операцію з дробями:
        if operation == '/':
            # Ділення однієї дробі на іншу еквівалентно множенню однієї дробі на перевернуту іншу,
            # тому перевертаємо значення екземпляру other:
            other.a, other.b = other.b, other.a
            # Проводимо операцію множення:
            self.a = other.a = int(self.a * other.a)
            self.b = other.b = int(self.b * other.b)
        elif operation == '*':
            self.a = other.a = int(self.a * other.a)
            self.b = other.b = int(self.b * other.b)
        elif operation == '+':
            self.a = other.a = int(self.a + other.a)
        elif operation == '-':
            self.a = other.a = int(self.a - other.a)
        # За можливості скорочуємо дроби:
        self.reduction_of_fractions(other)

    def __truediv__(self, other):
        """Метод, що виконує операцію ділення"""
        self.special_method(other, '/')
        return self

    def __mul__(self, other):
        """Метод, що виконує операцію множення"""
        self.special_method(other, '*')
        return self

    def __add__(self, other):
        """Метод, що виконує операцію додавання"""
        self.special_method(other, '+')
        return self

    def __sub__(self, other):
        """Метод, що виконує операцію віднімання"""
        self.special_method(other, '-')
        return self

    def __eq__(self, other):
        """Метод, що виконує операцію порівняння"""
        if self.__class__.__name__ == other.__class__.__name__ == Fraction.__name__:
            try:
                result =  (self.a / self.b) == (other.a / other.b)
            except ZeroDivisionError:
                print("ZeroDivisionError! (EQ)")
                result = False
        else:
            return False
        return result


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y == Fraction(3, 4))

    # Додаткові перевірки (не входять до умов завдання!)
    # x = Fraction(2, 3)
    # y = Fraction(1, 6)
    # x + y                     # 5/6  (2/3 + 1/6 = 4/6 + 1/6 = 5/6)
    # print(x.a, x.b)
    # x - y                     # 1/2  (2/3 - 1/6 = 4/6 - 1/6 = 3/6 = 1/2)
    # print(x.a, x.b)
    # x * y                     # 1/9  (2/3 * 1/6 = 2/18 = 1/9)
    # print(x.a, x.b)
    # x / y                     # 4/1  (2/3 / 1/6 = 2/3 * 6/1 = 12/3 = 4/1)
    # print(x.a, x.b)

    # x = Fraction(1, 3)
    # y = Fraction(2, 6)
    # print(x.__eq__(y))        # True

