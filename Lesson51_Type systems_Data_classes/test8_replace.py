from dataclasses import dataclass
from dataclasses import InitVar
from dataclasses import replace

@dataclass
class C:
    a: float
    b: float = None
    c: InitVar[float] = 2.0

    def __post_init__(self, c):
        print('HERE', self.c, c)
        self.b = self.a * c

x = C(2, c=3.0)
print(x)

y = replace(x, a=4, c=3.0)
print(y)
