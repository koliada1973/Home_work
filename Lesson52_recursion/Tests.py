def revers_str(string):
    if len(string) == 1:
        return string[0]
    else:
        return revers_str(string[1:]) + string[0]

print(revers_str('Wassamassaw – a town in South Dakota'))