def reverse(input_str: str):
    if len(input_str) == 1:
        return input_str
    else:
        return input_str[-1] + reverse(input_str[:-1])

print(reverse("hello") == 'olleh')
print(reverse("o") == "o")