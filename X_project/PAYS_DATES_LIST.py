from X_project.my_dates_funcs import *
# ===========================================================
# Використовуємо функцію PAYS_DATES_LIST для отримання списку усіх платежів договору
# Початкові дані: Start_date (дата відкриття договору)
#                 Srok (срок дії договору),
#                 Day_of_pay (день оплати),
#                 delta_days (допустима різниця між початковою датою договору та датою першої оплати)
# ===========================================================

# Створення нового номеру оплати
def f_next_number(list_pays: list) -> int:
    last_pay = list_pays[-1]
    return last_pay['number'] + 1


# Створення та заповнення словника оплати
def f_fill_payment(number: int, date: date, sum_pay: float, repayment_percent: float, sum_debt: float, sum_repayment: float, sum_remain: float) -> dict:
    payment = {
                'number': number,
                'date': date,
                'sum_pay': sum_pay,
                'repayment_percent': repayment_percent,
                'sum_debt': sum_debt,
                'sum_repayment': sum_repayment,
                'sum_remain': sum_remain,
                }
    return payment


# Розрахунок наступної оплати
def f_next_payment(number, date1: date, date2: date, sum_pay: float, Percent: float, sum_debt: float, sum_remain: float) -> dict:
    days = (date2 - date1).days
    sum_percent = round(sum_remain * days * Percent/100, 2)
    result_list =[]
    if sum_percent < 0:
        sum_percent = 0
    if sum_pay < sum_debt:
        sum_debt = round(sum_debt - sum_pay, 2)
        sum_remain = sum_remain
        repayment_percent = 0
        sum_repayment = 0
    elif sum_pay < (sum_debt + sum_percent):
        sum_debt = round(((sum_debt + sum_percent) - sum_pay), 2)
        repayment_percent = sum_pay
        sum_remain = sum_remain
        sum_repayment = 0
    else:
        sum_repayment = round(sum_pay - (sum_debt + sum_percent), 2)
        sum_remain = round(sum_remain - sum_repayment, 2)
        repayment_percent = sum_percent
        sum_debt = 0
    result_list = f_fill_payment(number, date2, sum_pay, repayment_percent, sum_debt, sum_repayment, sum_remain)
    return result_list


def f_pays_cycle_list(Start_date: date, Summa:float, Srok: int, Day_of_pay: int, Percent: float, delta_days = 10) -> list:
    """Функція, що повертає список словників оплат та усіх ключових дат договору"""
    
    # Дату першої оплати отримуємо окремо з використанням декоратора (присвоюємо змінній temp_func декоратор date_decorator1):
    temp_func = f_first_pay_decorator(add_months, Start_date, Day_of_pay, delta_days)
    # Дата першої оплати:
    first_pay_date = temp_func(Start_date, Day_of_pay, 1)
    # Дата останньої оплати за договором:
    last_pay_date = add_months(Start_date, Day_of_pay, Srok)
    # Початковий варіант суми оплати = Сума кредиту / Срок
    sum_pay = round(Summa * ((100 + Percent * 365) / 100) / Srok, 2)


    # Створюємо список оплат:
    LIST_PAYS_CYCLE = []
    # Перший рядок списку - дані на момент відкриття договору:
    LIST_PAYS_CYCLE.append(f_fill_payment(0, Start_date, 0, 0, 0, 0, Summa))
    # Другий рядок списку - перша оплата:
    pay_number = f_next_number(LIST_PAYS_CYCLE)
    LIST_PAYS_CYCLE.append(f_next_payment(pay_number, Start_date, first_pay_date, sum_pay, Percent, 0, Summa))
    # Заносимо наступні оплати:
    for i in range(Srok):
        last_dict = LIST_PAYS_CYCLE[-1]
        next_date = add_months(last_dict['date'], Day_of_pay, 1)
        if next_date <= last_pay_date:
            pay_number = f_next_number(LIST_PAYS_CYCLE)
            LIST_PAYS_CYCLE.append(f_next_payment(pay_number, last_dict['date'], next_date, sum_pay, Percent, last_dict['sum_debt'], last_dict['sum_remain']))
    return LIST_PAYS_CYCLE