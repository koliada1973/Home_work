def f1(List2):
    if len(List2) == 0:
        return
    else:
        f1(List2[1:])
        print(List2[0], end = ' ')

List1 = input('Введіть послідовність з N елементів через пробіл: ').split()
print(len(List1))
f1(List1)
