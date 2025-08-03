# Реалізуйте функцію (як параметр приймає клас), щоб виводила mro для цього класу уу форматі:
# A -> C -> D -> ...

def show_mro(class_name):
    list_mro = [a.__name__ for a in class_name.mro() if a is not object]
    return "->".join(list_mro)

class O: pass

class C(O): pass
class A(O): pass
class B(O): pass
class D(O): pass
class E(O): pass

class K1(C, A, B): pass
class K2(A, D): pass
class K3(B, D, E): pass

class Z(K1, K2, K3): pass


print(show_mro(Z))



class H:
    pass

class D(H):
    pass
class E(H):
    pass
class F(H):
    pass
class G(H):
    pass
class B(D, E):
    pass
class C(F, G):
    pass
class A(B, C):
    pass

print(show_mro(A))