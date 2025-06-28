def sum_of_digits(digit_string: str):
        if digit_string.isdigit():
            if len(digit_string) == 1:
                return int(digit_string[0])
            else:
                return int(digit_string[0]) + sum_of_digits(digit_string[1:])
        else:
            return "input string must be digit string"


print(sum_of_digits('26') == 8)
print(sum_of_digits('test'))