from dataclasses import dataclass

@dataclass
class MyClass:
    a: int
    b: str = ''

x = MyClass(1, 'hello')
x_clone = MyClass(1, 'hello')
y = MyClass(2, 'world')

print(x)
print(y)
print(x == x_clone)

q = MyClass(3)
wrong = MyClass('2', 1)

print(q)
print(wrong)

