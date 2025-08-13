from typing import List
from dataclasses import field, dataclass
from typing import ClassVar

@dataclass
class C:
    a: float
    b: float
    c: float = field(init=False)

    def __post_init__(self):
        self.c = self.a + self.b

x = C(2, 3)
print(x.c)

@dataclass
class C:
    a: float
    b: float
    c: float = field(init=False)

x = C(2, 3)
print(x.__dict__)