from sys import getsizeof

a = [i for i in range(10000)]
b = (i for i in range(10000))
# print(a)
# print(b)

# print()
# for i in a:
#     print(i)
#
# print()
# for i in b:
#     print(i)

print(getsizeof(a))
print(getsizeof(b))