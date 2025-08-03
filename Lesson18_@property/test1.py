class MyClass:
    attr = 1

    def __init__(self, attr):
        self.attr = attr

inst = MyClass('test')
# print(inst.attr)
# print(inst.__dict__)
# print(type(inst.__dict__))
# print(inst.attr == inst.__dict__['attr'])
# print(inst.__class__)
# print(inst.__class__.__dict__)
# print(inst.__class__.__dict__['attr'])
# print(inst.__dict__['attr'])

class MyBehaviorClass(MyClass):
    def print_attr(self):
        return self.attr

# print(MyClass.__dict__)
# print(inst.__dict__)

inst = MyBehaviorClass('Test')
print(inst.__dict__)
# print(inst.__class__.__dict__)
# print(MyBehaviorClass.__dict__)
# # print(MyBehaviorClass.__dict__['print_attr']())
#
# # print(inst.print_attr())
# print(MyBehaviorClass.print_attr(inst))
# print(inst.attr)
# print(MyBehaviorClass.attr)
del inst.attr
print(inst.__dict__)
print(inst.attr)
del MyClass.attr
print(inst.__dict__)
# print(inst.attr)
print(MyClass.__dict__)