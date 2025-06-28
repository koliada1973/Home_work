import string

letters = list(string.ascii_uppercase)
my_list = []
my_dict = {}
counter = 0

for i in range(10):
    for j in range(10):
        for letter in letters:
            my_list.append(str(i) + str(j) +letter)
            counter += 1
            my_dict.update({counter: my_list[-1]})

print('Кількість комбінацій: ', len(my_list))
print(my_dict)