import json

# Відкриваємо файл 'cj.json' та читаємо дані з файлу
with open('cj.json') as my_file:
    cj = json.load(my_file)
# print(cj)

# Отримуємо ключ та значення з кожної пари словника cj
for key, value in cj.items():
    if type(value) == list:     # Тут я обробляю вкладений в список словник...
        for i in value:
            print(key, end=': ')
            if type(i) == dict:
                for k, v in i.items():
                    print(f' {k}:{v} ', end = '')
                print()
    else:
        print(key, ' - ', value)