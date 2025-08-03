# Задача 4.
# Розсташуйте класи в порядку mro вручну, потім перевірте з допомогою методу mro.

class A: pass
class B: pass
class C: pass
class D(B, C): pass
class E(A, D): pass

cE = E()

print(cE.__class__.mro())