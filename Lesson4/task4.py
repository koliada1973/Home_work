# Task 4:
print('Task 4:')

name = 'сергій'

while True:
    # Отримуємо відповідь від користувача
    x = input("Назвіть моє ім'я: ")

    # Перевіряємо чи правильна відповідь і друкуємо повідомлення
    if  x.lower() == name.lower():
        print("Вірно, моє ім'я {}!".format(name.capitalize()))
        break
    else:
        print('Відповідь невірна!')
        #continue
