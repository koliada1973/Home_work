# Задача 1.
# Реалізувати:
# ·      ітератор (через клас),
# ·      функцію-генератор,
# ·      вираз-генератор
# для роботи з числами в діапазоні від 0 до 100 000 000 000, які без остачі діляться на 3 та на 7.
# Порівняйте розміри різних реалізацій (ітератор через клас, функція-генератор, вираз-генератор) при допомозі функції sys.getsizeof().
from sys import getsizeof

class MyIterator:
    def __init__(self, n):
        self.n = n
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= self.n:
                raise StopIteration
            self.index += 1
            if self.index % 3 == 0 and self.index % 7 == 0:
                return self.index

def my_generator(n):
    for i in range(n):
        if i % 3 ==0 and i % 7 == 0:
            yield i




N = 1000000
a = MyIterator(N)
b = my_generator(N)
c = (i for i in range(N) if i %3 == 0 and i % 7 ==0)
print(f"Сума елементів (клас ітератор) = {sum(a)}")
print(f"Сума елементів (генератор) = {sum(b)}")
print(f"Сума елементів (вираз-генератор) = {sum(c)}")
print(f"Розмір клас ітератор: {getsizeof(a)}")
print(f"Розмір генератор: {getsizeof(b)}")
print(f"Розмір вираз-генератор: {getsizeof(c)}")
