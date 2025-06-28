my_str = 'hello, world !'
my_str2 = 'привіт, світ !'

with open('file_1.txt', 'w', encoding="utf-8") as f:
    f.write(my_str + '\n')

with open('file_1.txt', 'a', encoding="utf-8") as f:
    f.write(my_str2 + '\n')