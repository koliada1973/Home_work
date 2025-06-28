def func1(list1):
    total = 0
    if len(list1) ==1:
        return list1[0]
    else:
        total = int(list1[0]) + int(func1(list1[1:]))
        return total

list2 = input('Insert int list: ').split()
print(func1(list2))
