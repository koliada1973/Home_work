# Задача 5.
# З порядком пошуку методів розібрались.
# А який порядок пошуку атрибутів ?
# З допомогою якої функції/методу можна отримати цей порядок ?
# Реалізуйте наслідування згідно схеми в рис.4.
# В кожного класу – однаковий атрибут description_attr, що містить ім“я класу,
# наприклад для класу A description_attr = „class A“.
# Перевірте порядок пошуку атрибутів, закоментовуючи цей атрибут, починаючи від класу А.

class H:
    # description_attr = "class H"
    pass

class D(H):
    # description_attr = "class D"
    pass

class E(H):
    # description_attr = "class E"
    pass

class F(H):
    # description_attr = "class F"
    pass

class G(H):
    # description_attr = "class G"
    pass

class B(D, E):
    # description_attr = "class B"
    pass

class C(F, G):
    # descrption_attr = "class C"
    pass

class A(B, C):
    # description_attr = "class A"
    pass

# A - B - D - E - C - F - G - H


cA = A()
# print(cA.description_attr)
print(cA.__class__.mro())
