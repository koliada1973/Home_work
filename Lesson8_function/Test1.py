# MINER_GAME
import random, colorama

# INIT colorama
colorama.init(autoreset = True)


# ----------------------------> GAME VALUES <-------------------------------
MAX_FIELD_SIZE = 10

# TEXT colors
GREEN_TEXT = colorama.Fore.GREEN
RED_TEXT = colorama.Fore.RED
YELLOW_TEXT = colorama.Fore.YELLOW
CYAN_TEXT = colorama.Fore.CYAN
MAGENTA_TEXT = colorama.Fore.MAGENTA
WHITE_TEXT = colorama.Fore.WHITE

# TEXT background colors
WHITE_BACK = colorama.Back.WHITE
CYAN_BACK = colorama.Back.CYAN
YELLOW_BACK = colorama.Back.YELLOW

field_size = MAX_FIELD_SIZE
bombs_number = 0
empty_cells_number = 0
opened_cells = 0


# ----------------------------> DEFINE FUNCTIONS <------------------------

# РАХУЄ кількість бомб навколо ячейки, якщо в ній немає бомби
def count_bomb_numbers(field, row, col):
    if field[row][col][0] != 'B':
        count_bombs = 0

        # ПЕРЕВІРКА лівого верхнього
        if row - 1 in range(field_size) and col - 1 in range(field_size) and field[row - 1][col - 1][0] == 'B':
            count_bombs += 1

        # ПЕРЕВІРКА центральнього верхнього
        if row - 1 in range(field_size) and field[row - 1][col][0] == 'B':
            count_bombs += 1

        # ПЕРЕВІРКА правого верхнього
        if row - 1 in range(field_size) and col + 1 in range(field_size) and field[row - 1][col + 1][0] == 'B':
            count_bombs += 1

        # ПЕРЕВІРКА центрального лівого
        if col - 1 in range(field_size) and field[row][col -1][0] == 'B':
            count_bombs += 1

        # ПЕРЕВІРКА центрального пправого
        if col + 1 in range(field_size) and field[row][col + 1][0] == 'B':
            count_bombs += 1

        # ПЕРЕВІРКА нижнього лівого
        if row + 1 in range(field_size) and col - 1 in range(field_size) and field[row + 1][col - 1][0] == 'B':
            count_bombs += 1

        # ПЕРЕВІРКА нижнього центрального
        if row + 1 in range(field_size) and field[row + 1][col][0] == 'B':
            count_bombs += 1

        # ПЕРЕВІРКА нижнього правого
        if row + 1 in range(field_size) and col + 1 in range(field_size) and field[row + 1][col + 1][0] == 'B':
            count_bombs += 1

        # print(count_bombs)
        return count_bombs
    return


# DISPLAY game field. Depending on arguments it can be fogged or not
def display_field(field, is_fogged):
    print(' |', end=' ')
    for i in range(field_size):
        print(i, end=' ')
    print()
    print('----------------------')
    for row in field:
        print(row, end='| ')
        for column in range(len(field[row])):
            is_open = field[row][column][1]
            cell = field[row][column][0]

            if is_fogged and not is_open:
                print(YELLOW_TEXT + 'X', end=' ')
            else:
                print((RED_TEXT if cell == 'B' else CYAN_TEXT) + str(cell), end=' ')


            # print('X' if is_fogged and not is_open else RED_TEXT + field[row][column][0], end=' ')
        print()


# -----------------------------> CREATE GAME STRUCTURE <--------------------------------------

# ASK USER FOR GAME SIZE
while True:
    game_size = input(f'Pls enter field size (min = 3, max = {MAX_FIELD_SIZE}): ').strip()

    if game_size.isdecimal():
        field_size = int(game_size)
        if field_size not in range(3, MAX_FIELD_SIZE + 1):
            print(YELLOW_TEXT + f'You have entered number not in range [{3};{MAX_FIELD_SIZE}], try again...')
            continue
        break
    else:
        print(RED_TEXT + f'You have entered not a decimal, try again...')
        continue


#CREATE game field and fill it with bombs
game_structure = {row: [] for row in range(field_size )}
for row in game_structure:
    for col in range(field_size):
        is_bomb = random.choice((0,1))
        if is_bomb == 1 !='B':
            game_structure[row].append(['B', False])
            bombs_number += 1
        else:
            game_structure[row].append(['0', False])

empty_cells_number = field_size * field_size - bombs_number
print(RED_TEXT + f'---> There was set {bombs_number} bombs on the field\n')
print(CYAN_TEXT + (f'---> There are {empty_cells_number} empty cells on the game field'))

# FILL empty cells with numbers of bombs around it
for row in game_structure:
    for col in range(field_size):
        count_bombs = count_bomb_numbers(game_structure, row, col)
        if count_bombs:
            game_structure[row][col][0] = count_bombs
# print()
# display_field(game_structure, False)

print()
display_field(game_structure, True)

# -----------------------> MAIN GAME LOOP <--------------------------------------

while True:
    # INPUT of row coordinates. CHECK if user wants to quit
    user_input_row = input('Pls enter ROW coord or "q" for quit: ').strip().lower()
    if user_input_row == 'q':
        print(MAGENTA_TEXT + 'YOU CHOSE TO QUIT. GOOD BYE!')
        display_field(game_structure, False)
        break
    elif user_input_row.isdecimal():
        user_input_row = int(user_input_row)
        if user_input_row not in range(field_size):
            print(YELLOW_TEXT + f'You have entered number not in range [{0};{field_size - 1}], try again...')
            continue
    else:
        print(RED_TEXT + f'You have entered not a decimal, try again...')
        continue

    # INPUT of column coordinates. CHECK if user wants to quit
    user_input_col = input('Pls enter COLUMN coord or "q" for quit: ').strip().lower()
    if user_input_col == 'q':
        print(MAGENTA_TEXT + 'YOU CHOSE TO QUIT. GOOD BYE!')
        display_field(game_structure, False)
        break
    elif user_input_col.isdecimal():
        user_input_col = int(user_input_col)
        if user_input_col not in range(field_size):
            print(YELLOW_TEXT + f'You have entered number not in range [{0};{field_size - 1}], try again...')
            continue
    else:
        print(RED_TEXT + f'You have entered not a decimal, try again...')
        continue

    # CHECK if user chose BOMB coordinates
    if game_structure[user_input_row][user_input_col][0] == 'B':
        print(RED_TEXT + '\n--------> GAME OVER!!! <--------\n')
        display_field(game_structure, False)
        break
    else:
        if not game_structure[user_input_row][user_input_col][1]: # if this cell is not already open
            game_structure[user_input_row][user_input_col][1] = True
            opened_cells += 1
        print(WHITE_TEXT + 'You opened ' + CYAN_TEXT+ f'{opened_cells}' + WHITE_TEXT + f' empty cells of {empty_cells_number}')


    if opened_cells == empty_cells_number:
        print(GREEN_TEXT + 'CONGRATULATIONS!!!\n' + MAGENTA_TEXT +  'YOU WON!!')
        display_field(game_structure, False)
        break

    display_field(game_structure, True)