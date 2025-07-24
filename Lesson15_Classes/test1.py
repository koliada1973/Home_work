# class MyClass:
#     class_attr = 0
#
# x = MyClass()
# y = MyClass()
#
# print(x.class_attr)     # 0
# print(y.class_attr)     # 0
#
# t = MyClass
# t.class_attr = 3
# print(x.class_attr)     # 3
# print(y.class_attr)     # 3
#
#
# x.class_attr = 1
# y.class_attr = 2
# print(x.class_attr)     # 1
# print(y.class_attr)     # 2
#
#
#
# print(t.class_attr)     # 3
#
# x.class_attr = 5
# y.class_attr = 6
#
# t.class_attr = 11
#
# print(x.class_attr)     # 5
# print(y.class_attr)     # 6
# print(t.class_attr)     # 11
#
# z = MyClass()
# print(z.class_attr)     # 11
# z.class_attr = 8
# print(z.class_attr)     # 8
# print(t.class_attr)     # 11
# print(x.class_attr)     # 5



class NewClass:
    class_attr = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def do_something(self, temp):
        print(f'A = {self.a}, B = {self.b}')
        return self.a + self.b, NewClass(self.a + self.b, self.a - self.b)

x = NewClass(1, 2)
y = NewClass(3, 4)

z =x.do_something(y)

print(z)

z = z[1]
print(z)
