import json
resume = {'name':'Serhii',
          'Last_name':'Koliada',
          'birth_date':'27.09.1973',
          'tel_number':'0979729385',
          'jobs':[{'Date1':'01.01.2000', 'position':'manager', 'salary':'20000'},
           {'Date2':'01.01.2000', 'position':'buhgalter', 'salary':'30000'},
           {'Date3':'01.01.2000', 'position':'director', 'salary':'40000'}]
          }

with open('resume.json', 'w', encoding="utf-8") as f:
    json.dump(resume, f, indent=4, ensure_ascii=False)

with open('resume.json', 'r', encoding="utf-8") as f:
    my_data = json.load(f)
    for k,job in enumerate(my_data['name']):
        # print(job)

        print("=== Резюме ===")
        print(f"Ім'я: {my_data['ім’я']}")
        print(f"Прізвище: {my_data['прізвище']}")
        print(f"Дата народження: {my_data['дата народження']}")
        print(f"Номер телефону: {my_data['номер телефону']}")

        print("\nМісця роботи:")
        for i, job in enumerate(my_data['місця роботи'], 1):
            print(f"\nМісце роботи #{i}:")
        print(f" Дата початку: {job['дата початку']}")
        print(f" Посада: {job['посада']}")
        print(f" Зарплата: {job['зарплата']}")