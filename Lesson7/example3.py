My_tuple = ()
i = 3

while i <= 231:
    if i % 13 == 0:
        My_tuple = My_tuple + (i,)
    i += 1

print(My_tuple)
