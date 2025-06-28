# Task 4:

Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

Dict1 = {Days.index(day) + 1 : day for day in Days}
Dict2 = {day : Days.index(day) + 1 for day in Days}

print(Dict1)
print(Dict2)