from dataclasses import dataclass
from dataclasses import InitVar

@dataclass
class C:
    a: float
    b: float = None
    c: InitVar[float] = 2.0

    def __post_init__(self, c):
        print('HERE', self.c, c)
        self.b = self.a * c

x = C(2, c=3.0)
print(x.__dict__)
print(x.c)
print(x.b)
