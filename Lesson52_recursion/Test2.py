from typing import Optional

def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
    if exp <= 0:
        raise ValueError("This function works only with exp > 0.")
    if x is None:
        return None
    return x ** exp


print(to_power(2, 3))