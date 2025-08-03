# Task 1:
# Перевантаження методів.
# Створіть базовий клас з іменем Animal з методом talk,
# а потім створіть два підкласи: Dog і Cat, і зробіть так, щоб реалізація методу talk у них відрізнялася.
# Наприклад, Dog може виводити "гав-гав", а Cat може виводити "няв".
# Також створіть просту узагальнену функцію, яка отримує на вхід екземпляри класів Cat або Dog і виконує метод talk над вхідним параметром.

class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        print("гав-гав")

class Cat(Animal):
    def talk(self):
        print("няв")

def do_talk(instance):
    instance.talk()

cat1 = Cat()
dog1 = Dog()

do_talk(cat1)
do_talk(dog1)