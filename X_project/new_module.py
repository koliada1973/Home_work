from X_project.my_dates_funcs import *
from X_project.PAYS_DATES_LIST import *

# Початкова дата - дата відкриття договору (поки використовуємо сьогоднішню дату):
Start_date = datetime.today().date()
# Start_date = date(2025, 7,31)   # А якщо в останній день місяця?
# День щомісячної оплати
Day_of_pay = 15
# Допустима різниця між початковою датою договору та датою першої оплати (не менше):
delta_days = 7
# Термін дії договору
Srok = 12
# Сума кредиту:
Summa = 30000
# Відсоткова ставка
Percent = 0.12

LIST_PAYS_CYCLE = f_pays_cycle_list(Start_date, Summa, Srok, Day_of_pay, Percent, delta_days)
for i in LIST_PAYS_CYCLE:
    print(i)




