from typing import List
from dataclasses import field, dataclass

@dataclass
class C:
    mylist: List[int] = field(default_factory=list)

c = C()
print('before', c.mylist)
c.mylist += [1, 2, 3]
print('after', c.mylist)


from typing import ClassVar
