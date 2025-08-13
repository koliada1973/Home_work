from typing import List
from dataclasses import field, dataclass
from typing import ClassVar

@dataclass
class MyClass:
    a: int = 1
    b: int = 1
    cls_var: ClassVar = 0

x = MyClass(2)
print(x.__dict__)
print(x.__class__.__dict__['cls_var'])
print("Look at result:", x.a + x.b * x.cls_var)


@dataclass
class MyClass:
    a: int = 1
    b: int = 1
    cls_var: ClassVar = 0

    def very_cool_method(self):
        return f"Look at result: {self.a + self.b * self.cls_var}"

x = MyClass(2)
print(x.very_cool_method())