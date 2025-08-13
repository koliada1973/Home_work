import time

# class longJorney:
#
#     def __init__(self):
#         self.val = self.calc_val()
#
#     def calc_val(self):
#         time.sleep(1)
#         return 42
#
# x = longJorney()
# y = longJorney()
# z = longJorney()

# print(x.val)

class MyAttr:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print("Get invoked")
        if instance is None:
            return self
        val = instance.calc_val()
        instance.__dict__[self.name] = val
        return val

class longJorney:
    val = MyAttr("val")

    def calc_val(self):
        time.sleep(1)
        return 42

x = longJorney()
y = longJorney()
z = longJorney()

print(x.__dict__)
print(x.val)
print(x.__dict__)
print(x.val)

print(x.__dict__)
# print(y.val)
# print(y.val)
# print(z.val)
# print(z.val)
longJorney.a = MyAttr('a')
print(longJorney.__dict__)
print(longJorney.a)
x = longJorney()
print(x.__dict__)
print(x.val)
print(x.a)
print(x.__dict__)