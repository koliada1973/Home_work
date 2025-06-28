# Task 1:
name = "serhii"
day = "saturday"

# Ім'я та день неділі робимо з великої букви
name = name[0].upper() + name[1:]
day = day[0].upper() + day[1:]

# Перший варіант фрази складаємо з f-strings:
str = f'Task 1:\n1 variant: Good day {name}! {day} is a perfect day to learn some python.'
print(str)
# Другий варіант фрази складаємо з format:
str = '2 variant: Good day {1}! {0} is a perfect day to learn some python.'.format(day, name)
print(str, end='\n\n')



# Task 2:
First_name = "Serhii"
Last_name = "Koliada"
print('Task 2:\nHi, ', First_name, ' ', Last_name, '!', sep="", end='\n\n')



# Task 3:
a = 8
b = 3
print('Task 3:\n8 + 3 =', a + b)
print('8 - 3 =', a - b)
print('8 / 3 =', a / b)
print('8 * 3 =', a * b)
print('8^3 =', a ** b)
print('ABS|-8| =', abs(-a))
print('8 // 3 =', a // b)
print('8 % 3 =', a % b)
