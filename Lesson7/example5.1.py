for i in range(-1, 11):
    if i < 0 :
        print('   | ', end='')
    elif i == 0 :
        print('---+-', end='')
    else:
        print(f'{i:<2} ', end = f'| ')
    for j in range(1, 11):
        if i < 0:
            print(f'{j:<3}', end=' ')
        elif i == 0:
            print('---', sep = '-', end='-')
        else:
            print(f'{i*j:<3}', end = ' ')
    print()
