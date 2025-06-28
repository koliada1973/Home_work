# Task 2:

def make_country(My_dict, country, capital):
    My_dict.update({country: capital})
    return My_dict

# Виклик функції з аргументами та друк отриманого результату
My_dict = {}
make_country(My_dict,'Ukraine', 'Kyiv')
make_country(My_dict,'Germany', 'Berlin')
print(My_dict)
print(My_dict['Ukraine'])

# Практичне використання результату
# Вилучення пари ключа та його значення для першої пари (індекс 0)
my_key, my_value = list(My_dict.items())[0]
print(f'{my_value} is the capital of {my_key}.')
# # Розширюємо словник
My_dict = make_country(My_dict,'Germany', 'Berlin')
print(My_dict['Germany'])
# # Вилучення окремо значення та окремо ключа для другої пари (індекс 1)
print(f'{list(My_dict.values())[1]} is the capital of {list(My_dict.keys())[1]}.')