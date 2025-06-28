def func1(list1):
    list2 = []
    for element in list1:
        if isinstance(element, list):
            list2.extend(func1(element))
        else:
            list2.append(element)
    return list2

print(func1([1, [2, 3, [4]], 5]))
print(func1([1, [2, 3], [[2], 5], 6]))
print(func1([[[[9]], [1, 2], [[8]]]]))