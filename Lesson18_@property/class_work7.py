# Task 1:
# Створіть клас Point з атрибутом x = 10.
# Створіть екземпляр і змініть значення атрибута x через __dict__.
# Надрукуйте значення до і після зміни.

class Point:
    x = 10

p = Point()
print("Task 1:")
print(p.__class__.__dict__['x'])
print(p.__class__.__dict__)
# p.__class__.__dict__['x'] = 15
# p.__class__.__dict__['x'] = 15 викликає помилку TypeError,
# оскільки __dict__ повертає спеціальний об'єкт mappingproxy,
# який є тільки для читання — тобто напряму змінювати його вміст не можна,
# але можна напряму (Point.x = 15) або через p.__class__:
p.__class__.x = 15
print(p.__class__.__dict__)
print()

# Task 2:
# Створіть простий дескриптор, який завжди повертає 100 при доступі.
# Підключіть його до класу Container і перевірте результат.

# Task 3:
# Створіть дескриптор, який дозволяє встановити значення лише більше 0.
# При спробі встановити неприпустиме значення — виводьте попередження.
class MyDescriptor:
    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.name] = value
        else:
            raise ValueError("value must be positive")

class MyClass:
    x = MyDescriptor('x')

    def __init__(self, x):
        self.x = x

a = MyClass(15)
print("Task 3:")
print(a.x)
print()

# Task 4:
# Створіть дескриптор SafeAttr, який викликає AttributeError,
# якщо атрибут ще не встановлено.
class SafeAttr:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, value):
        if instance is None:
            return value
        else:
            if self.name not in instance.__dict__:
                raise AttributeError(f"Атрибут '{self.name}' ще не встановлено")
            else:
                return instance.__dict__[self.name]

class MyClass:
    value = SafeAttr('value')

a = MyClass()
print("Task 4:")
try:
    print(a.value)
except AttributeError as e:
    print("Помилка: ", e)

a.value = 8
print(a.value)
print()

# Task 5:
# Продемонструйте, що data descriptor має вищий пріоритет, ніж атрибут у __dict__ екземпляра.
class MyDescriptor:
    def __get__(self, instance, owner):
        print("Метод  __get__ дескриптора")
        return 17

    def __set__(self, instance, value):
        print(f"метод __set__ дескриптора,  value = {value}")
        instance.__dict__['attr'] = value

class MyClass:
    attr = MyDescriptor()

obj = MyClass()
print("Task 5:")
obj.attr = 100
print(obj.__dict__)

print(obj.attr)


# Task 6:
# Створіть повноцінний дескриптор, який логуватиме дії з атрибутом:
# читання, запис і видалення.
class MyDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        print(f"Метод _get__ дескриптора для '{self.name}'")
        if self.name not in instance.__dict__:
            print(f"Атрибут '{self.name}' ще не встановлено")
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"Метод __set__ дескриптора. Запис {value} в атрибут '{self.name}' екземпляра {instance.__class__.__name__}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print(f"Метод __delete__ дескриптора. Видалення атрибута '{self.name}'")
        del instance.__dict__[self.name]

class MyClass:
    attr = MyDescriptor('attr')

print()
print("Task 6:")
a = MyClass()
a.attr = 135
print(a.attr)
del a.attr