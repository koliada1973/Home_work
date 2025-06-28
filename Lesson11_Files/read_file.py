# ЧИТАННЯ З ФАЙЛУ weekdays.txt

# Відкриття файлу 'weekdays.txt' для читання як змінна my_file та вичитування вмісту файлу
with open('weekdays.txt', 'r') as my_file:
    data_from_file = my_file.read() # В дужках можна вказати кількість символів, які потрібно зчитати
print(data_from_file)

# Відкриття файлу 'weekdays.txt' для читання як змінна my_file
# та построчне вичитування вмісту файлу як список, але із знаками перенесення рядка \n..:
# ['Monday\n', 'Tuesday\n', 'Wednesday\n', 'Thursday\n', 'Friday\n', 'Saturday\n', 'Sunday\n']
with open('weekdays.txt', 'r') as my_file:
    list_from_file = my_file.readlines()
print(type(data_from_file))

# Відкриття файлу 'weekdays.txt' для читання як змінна my_file
# та построчне вичитування вмісту файлу як список, з видаленям знаків перенесення рядка \n..:
# ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
with open('weekdays.txt', 'r') as my_file:
    list_from_file_new = []
    for day in my_file:
        list_from_file_new.append(day.rstrip())
    # list_from_file_new = [day.rstrip() for day in my_file.readlines()]  # КОМПРЕХЕНШН!
print(list_from_file_new)