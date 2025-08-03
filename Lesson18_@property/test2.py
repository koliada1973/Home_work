class MyAttr:
    def __get__(self, instance, owner):
        print("Get invoked")
        return 42
    def __set__(self, instance, value):
        print("Set invoked")


class Base:
    pass

Base.a = 1
Base.d = MyAttr()


print(Base.d)
print(Base.__dict__)

b = Base()
b.d = 20
print(b.d)
print(b.__dict__)
print(b.__class__.__mro__)

Base.d = 1
print(Base.d)
print(Base.__dict__)
b2 = Base()
b.d = 20
print(b2.d)