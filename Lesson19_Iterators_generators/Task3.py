# Task 3:
# Створіть власну реалізацію ітератора, який можна використовувати всередині циклу for-in.
# Також додайте логіку для отримання елементів за допомогою синтаксису квадратних дужок.

class MyIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= len(self.iterable):
                raise StopIteration
            self.index += 1
            return self.iterable[self.index - 1]

    def __getitem__(self, index):
        return self.iterable[index]


# Перевіряємо чи можливе отримання елементів за допомогою синтаксису квадратних дужок:
string = 'qwerty'
a = MyIterator(string)
print(MyIterator(string)[3])    # r
print(MyIterator(string)[:4])   # qwer
print(MyIterator(string)[-1])   # y
#
# # Чи працює як ітератор:
print()
list1 = [1,2,3,4,5,6,7,8,9]
x = MyIterator(list1)
print(next(x))  # 1
print(next(x))  # 2
print(next(x))  # 3

# В циклі:
print()
for i in x:
    print(i)