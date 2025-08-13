# Task 1:
# Створіть власну реалізацію вбудованої функції enumerate з назвою 'with_index',
# яка приймає два параметри: 'iterable' і 'start', за замовчуванням 0.
# Підказки: див. документацію до функції enumerate
#
# Довідка:   enumerate(iterable, start=0)
# (Метод __next__() ітератора, що повертається функцією enumerate(),
# повертає кортеж, що містить лічильник (зі старту, який за замовчуванням дорівнює 0)
# та значення, отримані в результаті ітерації над iterable.)

def with_index(iterable: any, start: int = 0) -> tuple:
    for i in iterable:
            yield (start, i)
            start += 1

list1 = ['1', 'qwerty', 25, [1, 2, 3]]

# Порівняємо списки, створені за допомогою with_index() та enumerate():
print(list(enumerate(list1)) == list(with_index(list1)))
# Для наочності друкуємо списки окремо:
print(list(with_index(list1)))
print(list(enumerate(list1)))