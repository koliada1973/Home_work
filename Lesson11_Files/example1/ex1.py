
my_str = 'hello, world !'
f = open('file_1.txt', 'w', encoding="utf-8")
f.write(my_str + '\n')
f.close()

my_str2 = 'привіт, світ !'
f = open('file_1.txt', 'a', encoding="utf-8")
f.write(my_str2 + '\n')

f.close()