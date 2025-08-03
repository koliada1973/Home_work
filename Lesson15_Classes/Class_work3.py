# Створіть модуль, в якому визначте функцію print(parametr), яка при її виклику буде друкувати „Hello ! I“m function print from {назва модуля}“ + parametr.
# Для реалізації print використовуйте sys.stdout.write(), попередньо імпортнувши модуль sys (інакше, реалізовуючи print через print будемо заходити в рекурсію).
# ·Імпортуйте функцію print в головну програму таким чином, щоб перезаписати вбудовний print
# ·викличіть функцію print, зверніть увагу на вивід.
# ·в головній програмі задайте функцію print(parametr), яка при її виклику буде друкувати „Hello ! I“m function print from {назва модуля}“ + parametr
# ·викличіть функцію print, зверніть увагу на вивід.
# ·p.s. На цьому прикладі має стати зрозуміло перезапис імен в межах одного простору імен та порядок пошуку імені в просторах імен.

from Class_work3_module import print



import sys
# def print(parametr):
#     # sys.stdout.write(f"Hello ! I'm function print from {__name__}\n + {parametr}")
#     # sys.stdout.write(parametr)
#     # print(f"Hello ! I'm function print from {__name__}\n")
#     print(parametr)


print("Bla-bla-bla")

def print(parametr):
    sys.stdout.write(f"Hello ! I'm function print from {__name__}\n + {parametr}")
    sys.stdout.write('\n')

print("Bla-bla-bla")
