import json
resume = {"Ім`я":'Сергій',
            'Фамілія':'Коляда',
            'Дата народження':'27.09.1973',
            'Телефон':'0979729385',
            'Дата1':{'Date':'01.01.2010', 'position':'manager', 'salary':'20000'},
            'Дата2':{'Date':'01.01.2020', 'position':'director', 'salary':'30000'}
          }

with open('resume.json', 'w', encoding="utf-8") as f:
    json.dump(resume, f, indent=4, ensure_ascii=False)

with open('resume.json', 'r', encoding="utf-8") as f:
    my_data = json.load(f)
    for k, values in my_data.items():
        if (k == 'Дата1' or k == 'Дата2') and type(values) == dict:
            print(k)
            for a, b in values.items():
                print (a, b)
        else:
            print(k, values)