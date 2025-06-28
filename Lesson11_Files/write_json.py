import json

# Словник різних даних про персону
cj = {}
cj['first_name'] = 'Carl'
cj['last_name'] = 'Jonson'
cj['has_a_dog'] = True
cj['has_a_pig'] = False
cj['cars'] = [{'brand':'Honda', 'model':'accord', 'color':'grey'}, {'brand':'Mercedes', 'model':'s500', 'color':'white'}]

# Створюємо файл cj.json та записуємо в нього словник cj:
with open('cj.json', 'w') as my_file:
    json.dump(cj, my_file)