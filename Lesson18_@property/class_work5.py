# Реалізувати додавання декількох чисел (к-сть від 1 до 10), як статичний метод.
# Принтити результат: перелік доданків, і суму

class MyClass:
    @staticmethod
    def my_add(*args):
        list1 = args
        result = sum(list1) if 1 < len(list1) <= 10 else None
        print(f"SUM({list1}) = {result}")

cl = MyClass()
cl.my_add(1, 2, 3, 4, 5, 6, 7)