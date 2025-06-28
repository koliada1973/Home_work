MIN_DRIVING_AGE = 18

def drivers(name, age):
    if age >= MIN_DRIVING_AGE:
        print(f'{name} може водити')
    else:
        print(f'{name} ще рано сідати за кермо')

drivers('Oleg', 16)