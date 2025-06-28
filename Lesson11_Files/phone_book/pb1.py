import json

def add_new_entries():
    first_name = input('Enter your first name: ').capitalize()
    last_name = input('Enter your last name: ').capitalize()
    telephone_number = input('Enter your telephone number: ')
    city = input('Enter your city: ')
    state = input('Enter your state: ')
    my_dict[telephone_number] = {'first_name': first_name,
                                 'last_name': last_name,
                                 'full_name' : first_name + ' ' + last_name,
                                 'city': city,
                                 'state': state}

def update_entries():
    first_name = input('Enter your new first name: ')
    last_name = input('Enter your new last name: ')
    city = input('Enter new city: ')
    state = input('Enter new state: ')
    telephone_number = search_result[0]
    print(search_result[1][first_name])
    if first_name == '':
        first_name = search_result[1][first_name]
    if last_name == '':
        last_name = search_result[1][last_name]
    if city == '':
        city = search_result[1][city]
    if state == '':
        state = search_result[1][state]

    my_dict[telephone_number] = {'first_name': first_name,
                                 'last_name': last_name,
                                 'full_name': first_name + ' ' + last_name,
                                 'city': city,
                                 'state': state}
    save_book()

def save_book():
    with open('pb.json', 'w', encoding='utf-8') as f_o:
        json.dump(my_dict, f_o, indent=4, ensure_ascii=False)

def show_book():
    print('______________________________________')
    for key in my_dict:
        print(key, ':', my_dict[key])
    print('______________________________________')

def search_entry(key, value):
    my_list = []
    if key == 'phone' and value in my_dict:
        return value, my_dict[value]
    else:
        result = []
        for k in my_dict:
            if value.lower() == my_dict[k][key].lower() :
                # my_list = (k, my_dict[k])
                # result.append(k)
                result.append((k, my_dict[k]))
            else:
                result = [(k, my_dict[k])]
        if len(result) > 0:
            return result
    return None


with open('pb.json', 'r', encoding='utf-8') as file_object:
    my_dict = json.load(file_object)

while True:
    my_choice = input('Do your choice, pls:\n'
                      '0 - program exit;\n'
                      '1 - Add new entries;\n'
                      '2 - SHOW phonebook;\n'
                      '3 - SEARCH by name;\n'
                      '4 - SEARCH by last name;\n'
                      '5 - SEARCH by fullname;\n'
                      '6 - SEARCH by phone;\n'
                      '7 - SEARCH by city;\n'
                      '8 - SEARCH by state;\n'
                      '9 - UPDATE by phone;\n'
                      )
    if my_choice == '0':
        break
    elif my_choice == '1':
        add_new_entries()
        save_book()
    elif my_choice == '2':
        show_book()
    elif my_choice == '3':
        print(search_entry('first_name', input('Pls enter the name for SEARCH: ')))
    elif my_choice == '4':
        print(search_entry('last_name', input('Pls enter the last name for SEARCH: ')))
    elif my_choice == '5':
        print(search_entry('full_name', input('Pls enter the full name for SEARCH: ')))
    elif my_choice == '6':
        search_result = search_entry('phone', input('Pls enter the phone for SEARCH: '))
        user = input('Do you want to update? y/n:  ')
        if user == 'y':
            update_entries()
    elif my_choice == '7':
        search_result = search_entry('city', input('Pls enter the city for SEARCH: '))
        for i in search_result:
            print(i)
    elif my_choice == '8':
        search_result = search_entry('state', input('Pls enter the state for SEARCH: '))
    elif my_choice == '9':
        user = input('Do you want to update? y/n:  ')
        if user == 'y':
            search_result = search_entry('phone', input('Pls enter the phone for SEARCH: '))
            update_entries()