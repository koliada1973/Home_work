# Task 3:
# Створіть власну реалізацію ітератора, який можна використовувати всередині циклу for-in.
# Також додайте логіку для отримання елементів за допомогою синтаксису квадратних дужок.

class MyIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0
        # У випадку, коли ітерабельний об'єкт - це множина, створюємо словник,
        # з якого можна отримувати елемент множини за ключем (індексом):
        self.iterable_list = []
        i = 0
        for element in iterable:
            self.iterable_list.append((i, element))
            i += 1

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= len(self.iterable):
                raise StopIteration
            self.index += 1
            # У випадку, коли ітерабельний об'єкт - це множина,
            # то повертаємо значення з iterable_dict по ключу index.
            # Інакше повертаємо елемент ітерабельного об'єкту за індексом:
            if isinstance(self.iterable, set):
                return self.iterable_list[self.index - 1][1]
            else:
                return self.iterable[self.index - 1]

    def __getitem__(self, index):
        if isinstance(index, slice):
            start = index.start
            stop = index.stop
            step = index.step
            if start is None:
                start = 0
            if step is None:
                step = 1
            string = ''
            for i in range(start, stop, step):
                if i < stop:
                    i += step
                    # string += self.iterable_list[i-1][1]
                    return self.iterable_list[i-1][1]
            # return string
        else:
            return self.iterable_list[index][1]
        # if isinstance(self.iterable, set):
        #     print('TypeError: object is not subscriptable')



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

print()
my_set = set(['1', 2])
s = MyIterator(my_set)
for i in s:
    print(i)

print()
# print(s[0])
print(s[0:])
# s = MyIterator(my_set)
# print(next(s))
# print(next(s))
# print(next(s))