def info_kwargs(**kwargs):
    list1 = sorted(kwargs)
    for key in list1:
        print(key, '=', kwargs[key])

info_kwargs(first_name="John", last_name="Doe", age=33)