class MyAttr:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print("Get invoked")
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print("Set invoked")
        if value > 0:
            instance.__dict__[self.name] = value
            return
        raise ValueError("Value must be > 0")

class ValidContainer:
    x = MyAttr('x')
    y = MyAttr('y')

    def __init__(self, a, b):
        self.x = a
        self.y = b

q = ValidContainer(1, 2)
print(q.x)
print(q.__dict__)