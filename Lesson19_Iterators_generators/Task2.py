# Task 2:
# Створіть власну реалізацію вбудованої функції range,
# назвавши її in_range(), яка приймає три параметри: 'start', 'end' і необов'язковий крок.
# Підказки: Зверніться до документації до функції range
#
# Довідка:  class range(start, stop[, step])
# Аргументи конструктора діапазону мають бути цілими числами
# (або вбудований int, або будь-який об'єкт, що реалізує спеціальний метод __index__()).
# Якщо аргумент step пропущено, то за замовчуванням він дорівнює 1.
# Якщо аргумент start пропущено, то за замовчуванням він дорівнює 0.
# Якщо step дорівнює нулю, то генерується ValueError.

class in_range:
    def __init__(self, start_: int =0, end_: int = 0, step_: int = 1):
        self.start = start_
        self.end = end_
        self.step = step_
        # Якщо step дорівнює нулю, то генерується ValueError
        if self.step == 0:
            raise ValueError("step не може дорівнювати нулю!")

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            result = self.start
            self.start += self.step
            return result
        else:
            raise StopIteration

# Порівняємо списки, створені за допомогою in_range() та range():
print([i for i in in_range(5, 100, 3)] == [x for x in range(5, 100, 3)])
# Для наочності друкуємо списки окремо:
print([i for i in in_range(5, 50, 3)])
print([x for x in range(5, 50, 3)])