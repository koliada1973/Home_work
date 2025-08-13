from typing import List
from dataclasses import field, dataclass
from typing import ClassVar


@dataclass
class Base:
    x: float = 15.0
    y: int = 0

@dataclass
class C(Base):
    z: int = 10
    x: int = 15

# The generated __init__() method for C will look like:
#
# def __init__(self, x: int = 15, y: int = 0, z: int = 10):