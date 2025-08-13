import json, sys

# Приймаємо другий аргумент (назва файлу) при запуску модуля з терміналу
# (перший аргумент - сам модуль)...
if len(sys.argv) > 1:
    file_name  = sys.argv[1]
else:
    file_name = 'phone_book.json'   # Значення за замовченням

# Функція, що зберігає телефонну книгу в файл
def save_book():
    with open(file_name, 'w', encoding='utf-8') as file_object:
        json.dump(my_book, file_object, indent=4, ensure_ascii=False)

# Функція, що отримує ID наступного запису контакта при додаванні нового контакта в телефонну книгу
# (знаходить найбільший ID в тел.книзі та кожного разу збільшує його на 1)...
def last_id():
    max_id = 0
    for key in my_book:
        id = int(key)
        if max_id <= id:
            max_id = id + 1
    return max_id

# Функція, що додає новий контакт в тел.книгу
# (запитує у користувача кожний елемент,
# зберігає в словник та викликає функцію запису в файл,
# а також викликає функцію, що друкує новий контакт...
def add_contact():
    contact = {'phone_number': "Введіть телефонний номер: ",
               'first_name':"Введіть ім'я: ",
               'last_name': "Введіть фамілію: ",
               'full_name': "",
               'state': "Введіть країну: ",
               'city': "Введіть місто: "
               }
    new_contact = {}
    new_id = last_id()
    for key, value in contact.items():
        user = ''
        if key == 'phone_number':
            user = input(value)
            if user.isdigit():
                new_contact.update({key: user})
            else:
                print('Помилка! Номер має складатись з цифр!')
                return
        elif key == 'full_name':
            f_name = new_contact['first_name'] + ' ' + new_contact['last_name']
            new_contact.update({key:f_name})
        elif key == 'first_name' or key == 'last_name':
            user = input(value)
            new_contact.update({key: user.capitalize()})
        else:
            user = input(value)
            new_contact.update({key: user})
    try:
        my_book[new_id] = new_contact
        save_book()
    except:
        print('Помилка при дадаванні контакту!')
    else:
        print('Контакт успішно додано!')
        print()
        print_contact({new_id:new_contact})

# Функція, що отримує від користувача ключ, за яким потрібно шукати контакт в тел.книзі,
# робить пошук та повертає результат пошуку...
def phone_book_search():
    text = '''Як шукати?:         За номером.........натисніть 1
                    За іменем..........натисніть 2
                    За фамілією........натисніть 3
                    За повним ім'ям....натисніть 4
                    За країною.........натисніть 5
                    За містом..........натисніть 6
                    
                    Повернутись............натисніть 0  ---> '''
    while True:
        user = input(text)
        print()
        if user == '1':
            search_key = 'phone_number'
            search_value = input("                    Введіть номер для пошуку: -------------> ")
            if search_value == '' or not search_value.isdigit():
                print('Перевірте дані, та спробуйте ще раз!: ')
                print()
                continue
            break
        elif user == '2':
            search_key = 'first_name'
            search_value = input("                    Введіть ім'я для пошуку: --------------> ").capitalize()
            if search_value == '':
                print('Перевірте дані, та спробуйте ще раз!: ')
                print()
                continue
            break
        elif user == '3':
            search_key = 'last_name'
            search_value = input("                    Введіть фамілію для пошуку: -----------> ").capitalize()
            if search_value == '':
                print('Перевірте дані, та спробуйте ще раз!: ')
                print()
                continue
            break
        elif user == '4':
            search_key = 'full_name'
            search_value = input("                    Введіть повне ім'я для пошуку: --------> ").capitalize()
            if search_value == '':
                print('Перевірте дані, та спробуйте ще раз!: ')
                print()
                continue
            break
        elif user == '5':
            search_key = 'state'
            search_value = input("                    Введіть країну для пошуку: ------------> ").capitalize()
            if search_value == '':
                print('Перевірте дані, та спробуйте ще раз!: ')
                print()
                continue
            break
        elif user == '6':
            search_key = 'city'
            search_value = input("                    Введіть місто для пошуку: -------------> ").capitalize()
            if search_value == '':
                print('Перевірте дані, та спробуйте ще раз!: ')
                print()
                continue
            break
        elif user == '0':
            return
        else:
            print('Введено помилкове значення!')
            print()
            continue
    result = {}
    for id, value in my_book.items() :
        if search_value.capitalize() in value[search_key]:   # Якщо і ключ і значення відповідають заданим - контакт знайдено
            result[id] = value
    return result

# Функція, що змінює існуючі дані в тел.книзі:
# отримує від користувача значення по кожному ключу
# та викликає функцію, що зберігає зміни в файл...
def phone_book_update(contact):
    for key, value in contact.items():
        print()
        for k, v in value.items():
            try:
                if k != 'full_name':
                    last_v = v
                    user = input(f'Внесіть нове значення {k} замість {v}: ')
                    if user != '':
                        value[k] = user
                    else:
                        v = last_v
                elif k == 'full_name':
                    value[k] = value['first_name'] + ' ' + value['last_name']
            except:
                print('Помилка під час оновлення даних!')
        # my_book[key] = value
        # save_book()
    return contact

# Функція, що видаляє записи з тел.книги...
def phone_book_delete(contact):
    user = input('Ви дійсно хочете видалити контакт? y/n: ')
    if user == 'n':
        return
    else:
        for key, value in contact.items():
            try:
                my_book.pop(key)
                save_book()
            except:
                print('Помилка видалення!')
            else:
                print('Контакт видалено!')

# Функція, що виводить на друк контакти
# (у випадку, коли кілька контактів відповідають критерію пошуку - виводить на друк їх всі)
def print_contact(contact):
    print('Результат: ')
    for key, value in contact.items():
        for k, v in value.items():
            s = '.'*(70 - (len(k) + len(v)))
            print(f'{k}{s}{v}')
        print()

# Функція, що друкує весь зміст тел.книги (Батир)
def show_book():
    print('______________________________________')
    for key in my_book:
        print(key, ':', my_book[key])
    print('______________________________________')

# Функція main, що комунікує з користувачем
# та в свою чергу викликає інші функції...
def main():
    global my_book
    text = '''
Виберіть опцію:     Додати контакт.....натисніть 1
                    Знайти контакт.....натисніть 2
                    Змінити контакт....натисніть 3
                    Видалити контакт...натисніть 4
                    Показати все.......натисніть 5

                    Вийти з програми.......натисніть 0  ---> '''

    text2 = '''
Виберіть опцію:     Змінити контакт....натисніть 3
                    Видалити контакт...натисніть 4
    
                    Повернутись........натисніть 0  -------> '''

    result_dict = {}
    # Відкриття файлу телефонної книги. Якщо файл не існює - створюємо його та записуємо в нього {}:
    try:
        with open(file_name, 'r', encoding='utf-8') as file_object:
            my_book = json.load(file_object)
    except FileNotFoundError:
        with open(file_name, 'w', encoding='utf-8') as file_object:
            json.dump({}, file_object, ensure_ascii=False, indent=4)
        my_book = {}

    while True:
        user = input(text)
        if user == '0':
            save_book()
            print("Зупиняємо програму...")
            break
        elif user == '1':
            print()
            add_contact()
            save_book()
        elif user == '2':
            print()
            contact = phone_book_search()
            if contact == {}:
                print('Контакт не знайдено...')
            elif contact == None:
                print('Повертаємось...')
            else:
                print_contact(contact)
                user2 = input(text2)
                if user2 == '0':
                    save_book()
                    print("Повертаємось...")
                elif user2 == '3':
                    contact = phone_book_update(contact)
                    save_book()
                    print()
                    print('Дані контакту успішно змінено:')
                    print_contact(contact)
                elif user2 == '4':
                    contact = phone_book_delete(contact)
                    save_book()
        elif user == '3':
            print()
            try:
                contact = phone_book_search()
                print_contact(contact)
            except:
                print('Помилка під час пошуку!')
            else:
                print('Контакт знайдено...')
            contact = phone_book_update(contact)
            save_book()
            print()
            print('Дані контакту успішно змінено:')
            print_contact(contact)
        elif user == '4':
            print()
            try:
                contact = phone_book_search()
            except:
                print('Помилка під час пошуку!')
            else:
                print('Контакт знайдено...')
            contact = phone_book_delete(contact)
        elif user == '5':
            show_book()

if __name__ == '__main__':
    main()