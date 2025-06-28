import random
from logging import lastResort

field = {}
# count_bombs = 0

# Розкладуємо міни
Last_mine = 0
Last_step = 0
for x in range(8):
    a = random.randint(0, 7)
    for y in range(8):
        if a == y:
            field[(x, y)] = ['B', True]
            Last_mine += 1
        else:
            field[(x, y)] = [0, True]
            Last_step += 1
# Рахуємо скільки мін в сусідніх клітинках
for key in field.keys():
    if field[key][0] != 'B':
        count_bombs = 0
        for shift_x in range(-1,2):
            for shift_y in range(-1,2):
                if 0 <= key[0] + shift_x < 8 and 0 <= key[1] + shift_y < 8:
                    if field[(key[0] +shift_x, key[1] + shift_y)][0] == 'B':
                        count_bombs += 1
        field[key][0] = count_bombs

while Last_step > 0:
    for x in range(8):
        for y in range(8):
            if field[(x, y)][1] == False:
                print(f'{field[(x, y)][0]:>2}', end=' ')
            else:
                print(f'{'X':>2}', end=' ')
        print()

    # Запит координат від користувача і перевірка введених даних
    User_X = input('Введіть коордінати Х (число від 1 до 8), або q для виходу: ')
    User_Y = input('Введіть коордінати Y (число від 1 до 8), або q для виходу: ')
    if User_X == 'q' or User_Y == 'q':
        print('Ви ввели q для виходу.')
        break
    elif User_Y.isalpha() or User_Y.isalpha():
        print('Всі координати мають бути цілими числами. Спробуйте ще раз..')
        continue
    elif User_X == '' or User_Y == '':
        print('Ви ввели пусту строку. Спробуйте ще раз..')
        continue
    elif int(User_X) == 0 or int(User_Y) == 0 or int(User_X) > 8 or int(User_Y) > 8:
        print('Координати мають бути більше 0 та не більше 8. Спробуйте ще раз..')
        continue
    else:
        # Координати користувача перетворюємо в цілі числа та відмічаємо клітинку як відкриту (Закрита = False)
        Last_step -= 1
        User_X = int(User_X)-1
        User_Y = int(User_Y)-1
        field[User_X, User_Y][1] = False
        # Якщо клітинка замінована - кінець гри, в іншому випадку ідемо на новий цикл
        if field[User_X, User_Y][0] == 'B':
            field[User_X, User_Y][1] = False
            print('Ви програли!')
            break
        elif Last_step <= 0:
            print('Поздоровляємо! Ви виграли!')
            break

# Друк мінного поля з результатами
for x in range(8):
    for y in range(8):
        if field[(x, y)][1] == False:
            print(f'{field
            [(x, y)][0]:>2}', end=' ')
        else:
            print(f'{'X':>2}', end=' ')
    print()