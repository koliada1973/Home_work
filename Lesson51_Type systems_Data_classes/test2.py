from typing import List
from dataclasses import field, dataclass


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class MyClass:
    a: int = 1
    b: int = 1

@dataclass(init=True, repr=True, eq=True, order=True)
class MyClass:
    a: int = 1
    b: int = 1

x = MyClass(1, 1)
y = MyClass(2, 1)

print(x < y)

from dataclasses import asdict, astuple

print(astuple(x))
print(astuple(y))
print(astuple(y) > astuple(x))

print(asdict(x))
print(asdict(y))

@dataclass(init=True, repr=True, eq=True, order=True, frozen=True)
class MyClass:
    a: int = 1
    b: int = 1

x = MyClass(1, 1)
# x.a = 100
# x.c = 101

