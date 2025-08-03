class First:
    def __init__(self, attr_first):
        self.attr_first = attr_first
        self._protected_attr = 0
        self.__private_attr = 1000

    def _protected_method(self):
        print('First._protected_method')

    def __private_method(self):
        print('First._private_method')

    def protected_test_method(self):
        self._protected_method()
        print(f'First._protected_attr: {self._protected_attr}')

    def private_test_method(self):
        self.__private_method()
        print(f'First._private_attr: {self.__private_attr}')

class FirstProtected(First):
    def protected_test_method(self):
        self._protected_method()
        print(f'First._protected_attr: {self._protected_attr}')

class FirstPrivate(First):
    def private_test_method(self):
        # self.__private_method()
        print(f'First._private_attr: {self.__private_attr}')

# first = First('f')
# first._protected_method()
# print('*'*20)
# print(first._protected_attr)
# first.test_method()
# print('*'*20)
# first_protected = FirstProtected('f')
# first_protected.test_method()


# first = First('f')
# first._First__private_method()
# print(first._First__private_attr)
# print('*'*20)
# print(first._protected_attr)
# first.private_test_method()

# print('*'*20)
# first_private = FirstPrivate('f')
# first_private.private_test_method()

class Product(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # def __add__(self, other):
    #     return self.price + other.price


product_1 = Product('Apple', 100)
product_2 = Product('Apple', 100)

print(product_1 == product_1)
print(id(product_1))
print(id(product_2))
