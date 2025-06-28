def check_password(password):
    sum_d = sum(a.isdigit() for a in password)
    char_A = any(a.isupper() for a in password)
    my_set = False
    for a in password:
        my_set = True if a in "!@#$%%*" else False

    if sum_d >= 3 and char_A and my_set and len(password) >= 10:
        print("Perfect password")
    else:
        print("Easy peasy")

check_password('Abcd123*12')