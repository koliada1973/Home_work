# Функція reverse тут для прикладу імпорту з модуля
def reverse_recurs(input_str: str):
    if len(input_str) == 1:
        return input_str
    else:
        return input_str[-1] + reverse_recurs(input_str[:-1])

# Функція main запускається на виконання тільки при відкритті модуля, не при імпорті
def main():
    print(reverse_recurs('A.B.C.D.E'))
    # Something working ...

# Цей запис гарантує, що при імпорті модуля функція main запускатись не буде
# (а вкладені функції імпортуватись будуть), а при відкритті модуля - буде
if __name__ == "__main__":
    main()
