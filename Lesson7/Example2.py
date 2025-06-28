My_tuple = ()

for i in range(3, 232):
    if i % 13 == 0:
        My_tuple = My_tuple + (i,)

print(My_tuple)