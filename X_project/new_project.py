from datetime import datetime, timedelta, date
import sys
from my_dates_funcs import *

# Примітивний розрахунок планового платежу
def primitive_pay(matrix_list, params) -> float:
    """Функція повертає примітивний (початковий) варіант суми оплати  -
    сумма з усіма відсотками за весь срок кредиту, поділена на срок.
    Тобто платіж = (сума кредиту + відсотки за весь срок) / срок"""
    delta_days = (matrix_list[-1]['date'] - matrix_list[0]['date']).days
    pay = round((params['Summa'] + (params['Summa'] * params['Percent'] * delta_days/100))/params['Srok'], 2)
    return pay
# Перевірка чи можливо текст перетворити на дробне число:
def is_float(s) -> bool:
    """Функція перевіряє текстовий рядок, чи можливо його перетворити в число з комою"""
    try:
        float(s)
        return True
    except ValueError:
        return False
# Перетворення тексту в дробне число:
def parse_float(text) -> float:
    if is_float(text):
        return float(text)
    else:
        print(f'Рядок {text} не можливо перетворити в float')
# Перевірка чи можливо текст перетворити на число:
def is_int(s) -> bool:
    """Функція перевіряє текстовий рядок, чи можливо його перетворити в число"""
    try:
        int(s)
        return True
    except ValueError:
        return False
# Перетворення тексту в число:
def parse_int(text) -> int:
    if is_int(text):
        return int(text)
    else:
        print(f'Рядок {text} не можливо перетворити в int')
# Перетворення параметрів, що надані при запуску модуля, на значення:
def parse_params(params:dict, result:dict):
    """Функція перевіряє початкові аргументи, що були передані при запуску модуля,
    та перетворює їх з текстового рядку в значення"""
    # Чи були передані початкові аргументи при запуску модуля через командний рядок:
    if params:
        params_ok = True
    else:
        params_ok = False
    # Перевіряємо кожний параметр, якщо він був передан - перетворюємо текст в значення та зберігаємо в результівному словнику
    if 'start_date' in params:
        result['Start_date'] = f_parse_date(params['start_date'])
    else:
        result.update({'Start_date':None})
        params_ok = False
    if 'first_pay_date' in params:
        result['First_pay_date'] = f_parse_date(params['first_pay_date'])
    else:
        result.update({'First_pay_date':None})
        params_ok = False
    if 'summa' in params:
        result['Summa'] = parse_float(params['summa'])
    else:
        result.update({'Summa':None})
        params_ok = False
    if 'srok' in params:
        result['Srok'] = parse_int(params['srok'])
    else:
        result.update({'Srok':None})
        params_ok = False
    if 'percent' in params:
        result['Percent'] = parse_float(params['percent'])
    else:
        result.update({'Percent':None})
        params_ok = False
    if 'day_of_pay' in params:
        result['Day_of_pay'] = parse_int(params['day_of_pay'])
    else:
        result.update({'Day_of_pay':None})
        params_ok = False
    return params_ok
# Отримання відсутніх параметрів:
def get_missing_data(dict1) -> dict:
    """Функція перевіряє переданий в функцію словник параметрів
    і якщо параметру не достає - запитує дані у користувача"""
    Start_date = datetime.today().date()
    text_start_date = f_format_date_ua(datetime.today().date())
    data_from_the_user = {
        'Start_date': f"Прийняти {text_start_date} за начальну дату договору - 0; або введіть свій варіант: --> ",
        'Day_of_pay': "Введіть день щомісячної оплати --> ",
        'First_pay_date': "",
        'Summa': "Введіть суму кредиту, грн. --> ",
        'Srok': "Введіть термін кредиту, місяці --> ",
        'Percent': "Введіть % ставку за добу --> "
        }
    for key, value in data_from_the_user.items():
        user = ''
        if key == 'Start_date':
            if dict1[key] is None:
                user = input(value)
                if user == '0':
                    dict1[key] = Start_date
                else:
                    # Обробляємо відповідь користувача в функції f_parse_date і отримуємо дату
                    user = f_parse_date(user)
                    # Якщо відповідь від користувача зрозуміти не вдалось (повернулось None):
                    if user == None:
                        dict1[key] = Start_date
                    else:
                        dict1[key] = user
        elif key == 'Srok' or key == 'Day_of_pay':
            if dict1[key] is None:
                user = input(value)
                if user.isdigit():
                    # data_from_the_user.update({key: int(user)})
                    dict1[key] = parse_int(user)
        elif key == 'Summa':
            if dict1[key] is None:
                user = input(value)
                if user.isdigit():
                    # data_from_the_user.update({key: float(user)})
                    dict1[key] = parse_float(user)
        elif key == 'Percent':
            if dict1[key] is None:
                user = input(value)
                user = user.replace(",", ".")
                user = user.replace("/", ".")
                if is_float(user):
                    # data_from_the_user.update({key: float(user)})
                    dict1[key] = dict1[key] = parse_float(user)
        elif key == 'First_pay_date':
            if dict1[key] is None:
                # Дату першої оплати отримуємо окремо з використанням декоратора (присвоюємо змінній temp_func декоратор f_first_pay_decorator):
                temp_func = f_first_pay_decorator(add_months, dict1['Start_date'],dict1['Day_of_pay'])
                # Дата першої оплати:
                # data_from_the_user.update({'First_pay_date': temp_func(data_from_the_user['Start_date'], data_from_the_user['Day_of_pay'],1)})
                dict1[key] = temp_func(data_from_the_user['Start_date'], data_from_the_user['Day_of_pay'],1)
    return dict1
# Отримання початкових даних для розрахунку:
def get_start_data(args) -> dict:
    """Функція повертає словник з початковими даними для подальшого розрахунку"""
    params = {}
    # Отримуємо список початкових даних, переданих як аргументи при запуску модуля
    # (допустимо розділяти ключ та значення за допомогою '=' або ':'):
    for arg in args:
        if '=' in arg:
            key, value = arg.split('=', 1)
            params[key] = value
        elif ':' in arg:
            key, value = arg.split(':', 1)
            params[key] = value
    # Якщо при запуску модуля були передані початкові аргументи,
    # то ці дані потрібно перетворити з тексту в значення
    result = {}
    # Перевіряємо отримані дані та перетворюємо їх на значення за допомогою функції parse_params:
    params_ok = parse_params(params, result)
    # Якщо всі дані в порядку, то повертаємо словник з початковими параметрами (ключ:значення)
    if params_ok:
        return result
    # Якщо якихось даних не вистачає - запитуємо у користувача за допомогою функції get_missing_data
    elif params_ok == False:
        return get_missing_data(result)
# Заповнення словника даних платежу:
def fill_payment_dict(date: date, pay: float, rep_percent: float, debt: float, rep_ostatok: float, ostatok: float) -> dict:
    payment_dict = {
                'date': date,
                'pay': pay,
                'rep_percent': rep_percent,
                'debt': debt,
                'rep_ostatok': rep_ostatok,
                'ostatok': ostatok
                }
    return payment_dict
# Отримання пустого списку платежів:
def get_empty_pays_list(params) -> list:
    """Функція повертає список усіх ключових дат кредиту"""
    empty_matrix = []
    # Додаємо в матрицю словник попереднього платежу (тільки початкова дата та сума кредиту)
    empty_matrix.append(fill_payment_dict(params['Start_date'], 0, 0, 0, 0, params['Summa']))
    # Додаємо в матрицю словник першого платежу (тільки дата першої та сума кредиту)
    empty_matrix.append(fill_payment_dict(params['First_pay_date'], 0, 0, 0, 0, 0))
    # Кінцева дата кредиту
    End_date = add_months(params['Start_date'], params['Day_of_pay'], params['Srok'])
    # Заповнюємо матрицю з датами наступних платежів
    for i in range(params['Srok']):
        last_date = empty_matrix[-1]['date']
        next_date = add_months(last_date, params['Day_of_pay'], 1)
        if next_date <= End_date:
            empty_matrix.append(fill_payment_dict(next_date, 0, 0, 0, 0, 0))
    return empty_matrix
# Розрахунок наступного платежу:
def next_payment(date1: date, date2: date, pay: float, percent: float, debt: float, ostatok: float, flag=False) -> dict:
    """Функція, що заповнює словник одного платежу (рядка).
    Параметр flag=True ставить залишок = 0 у випадку від'ємного залишку на кінці"""
    delta_days = (date2 - date1).days
    sum_procent = round(ostatok * delta_days * percent/100, 2)
    result_list =[]
    if sum_procent < 0:
        rep_percent = 0
    if pay < debt:
        debt = round(debt + (debt - pay), 2)
        ostatok = ostatok
        rep_percent = 0
        rep_ostatok = 0
    elif pay <= (debt + sum_procent):
        rep_percent = round(pay - debt, 2)
        # rep_percent = round(sum_procent - (sum_procent - (pay - debt)), 2)
        rep_ostatok = 0
        if rep_percent < 0:
            rep_percent = 0
        debt = round(((debt + sum_procent) - pay), 2)
        ostatok = ostatok
    else:
        if flag and pay >= (ostatok + debt + sum_procent):
            rep_ostatok = ostatok
            rep_percent = sum_procent
            ostatok = 0
            debt = 0
            pay = round(rep_ostatok + rep_percent, 2)
        else:
            rep_ostatok = round(pay - (debt + sum_procent), 2)
            ostatok = round(ostatok - rep_ostatok, 2)
            rep_percent = sum_procent
            debt = 0
    return fill_payment_dict(date2, pay, rep_percent, debt, rep_ostatok, ostatok)
# Розрахунок циклу всіх платежів
def cycle_payments(matrix_list, useful_data, params) -> list:
    copy_matrix_list = matrix_list.copy()
    pre_payment = copy_matrix_list[0]
    for i, payment_dict in enumerate(copy_matrix_list):
        if i >= 1:
            next_date = payment_dict['date']
            if next_date <= copy_matrix_list[-1]['date']:
                payment_dict = next_payment(pre_payment['date'], next_date, useful_data['pay2'], params['Percent'], pre_payment['debt'], pre_payment['ostatok'], useful_data['end_flag'])
                pre_payment = payment_dict
                copy_matrix_list[i] = payment_dict
    return copy_matrix_list
# Розрахунок наступного платежу методом інтерполяції:
def interpolation_new_pay(useful_data) -> float:
    """Функція знаходить новий платіж методом інтерполяції"""
    # if useful_data['ostatok2'] == useful_data['ostatok1']:
    #     return useful_data['pay2']
    if abs(useful_data['pay1'] - useful_data['pay2']) <= 0.01 or abs(useful_data['ostatok2'] - useful_data['ostatok1']) < 0.01 and abs(useful_data['ostatok2'] - useful_data['ostatok1']) > 0:
        new_pay = useful_data['min_pay'] + ((useful_data['max_pay'] - useful_data['min_pay']) / (useful_data['max_ostatok'] - useful_data['min_ostatok'])) * (-0.01 - useful_data['min_ostatok'])
    else:
        new_pay = useful_data['pay1'] + ((useful_data['pay2'] - useful_data['pay1']) / (useful_data['ostatok2'] - useful_data['ostatok1'])) * (-0.01 - useful_data['ostatok1'])
    # if new_pay <= 0:
    #     new_pay = 0.01
    return new_pay
# Розрахунок зміненого варіанту платежу:
def get_changed_payment(useful_data) -> float:
    if ((useful_data['ostatok1'] <= useful_data['min_ostatok']
        or useful_data['ostatok1'] >= useful_data['max_ostatok']
        or useful_data['ostatok2'] <= useful_data['min_ostatok']
        or useful_data['ostatok2'] >= useful_data['max_ostatok'])
            and useful_data['pay1'] != useful_data['pay2']
            and (abs(useful_data['ostatok1']) > useful_data['max_pay']
                 or abs(useful_data['ostatok2']) > useful_data['max_pay'])):
        return (useful_data['max_pay'] + useful_data['min_pay']) / 2
    elif -0.01 < useful_data['ostatok2'] <= 0.01 and abs(useful_data['pay1'] - useful_data['pay2']) <= 0.01:
        if useful_data['ostatok2'] >= -0.01:
            useful_data['pay2'] = useful_data['pay2'] + 0.01
            return useful_data['pay2']
        elif useful_data['ostatok2'] < 0:
            return useful_data['pay2']
    elif useful_data['ostatok1'] == useful_data['ostatok2'] and useful_data['ostatok1'] > 0:
        return useful_data['max_pay'] + 0.01
    else:
        return interpolation_new_pay(useful_data)
# Перевірка чи досягнуто потрібного залишку під час пошуку платежу:
def ostatok_is_ok(useful_data) -> bool:
    if abs(useful_data['pay1'] - useful_data['pay2']) <= 0.01 and min(useful_data['ostatok1'], useful_data['ostatok2']) <= 0.01 and max(useful_data['ostatok1'], useful_data['ostatok2']) > 0 and abs(min(useful_data['ostatok1'], useful_data['ostatok2'])) < min(useful_data['pay1'], useful_data['pay2']):
        return True
    elif -0.01 < min(useful_data['ostatok1'], useful_data['ostatok2']) <= 0.01 or -0.01 < max(useful_data['ostatok1'], useful_data['ostatok2']) <= 0.01 and abs(min(useful_data['ostatok1'], useful_data['ostatok2'])) < min(useful_data['pay1'], useful_data['pay2']):
        return True
    elif abs(useful_data['pay1'] - useful_data['pay2']) <= 0.0001 and min(useful_data['ostatok1'], useful_data['ostatok2']) <= 0.0001 and abs(min(useful_data['ostatok1'], useful_data['ostatok2'])) < min(useful_data['pay1'], useful_data['pay2']):
        return True
    elif abs(useful_data['pay1'] - useful_data['pay2']) <= 0.001 and max(useful_data['ostatok1'], useful_data['ostatok2']) < 0 and useful_data['ostatok1'] == useful_data['ostatok2']:
        return True
    else:
        return False
# Заповнення словнику даних для подальшого використання:
def fill_useful_data(params) -> dict:
    return {'pay1': 0,
           'pay2': 0,
           'ostatok1': params['Summa'],
           'ostatok2': params['Summa'],
           'min_pay': 0,
           'max_pay': 0,
           'min_ostatok': params['Summa'],
           'max_ostatok': params['Summa'],
           'end_flag': False}
# Вибір найбільш догідного залишку:
def best_ostatok(ostatok1, ostatok2):
    min_ost = min(ostatok1, ostatok2)
    max_ost = max(ostatok1, ostatok2)
    if min_ost <= 0 and max_ost <= 0:
        a = min(abs(min_ost), abs(max_ost))
        if a == abs(ostatok1):
            return ostatok1
        elif a == abs(ostatok2):
            return ostatok2
    else:
        return min_ost
# Перерахунок useful_data (макс/мін залишку, макс/мін платежу) після кожної ітерації підбору
def renew_useful_data(useful_data, new_pay, new_ostatok):
    if new_ostatok >= useful_data['max_ostatok'] and new_pay > useful_data['min_pay']:
        useful_data['min_pay'] = new_pay
        useful_data['max_ostatok'] = new_ostatok
    elif new_ostatok < useful_data['max_ostatok'] and new_ostatok > 0.01 and new_pay > useful_data['min_pay']:
        useful_data['min_pay'] = new_pay
        useful_data['max_ostatok'] = new_ostatok
    if new_ostatok <= useful_data['min_ostatok'] and new_pay < useful_data['max_pay'] and new_ostatok != useful_data[
        'max_ostatok']:
        useful_data['max_pay'] = new_pay
        useful_data['min_ostatok'] = new_ostatok
    elif new_ostatok > useful_data['min_ostatok'] and new_ostatok < 0.01 and new_pay < useful_data['max_pay']:
        useful_data['max_pay'] = new_pay
        useful_data['min_ostatok'] = new_ostatok
    if new_ostatok == useful_data['max_ostatok'] == useful_data['ostatok1'] == useful_data['ostatok2']:
        useful_data['max_pay'] = useful_data['max_pay'] * 1.1
    useful_data['ostatok1'] = useful_data['ostatok2']
    useful_data['ostatok2'] = new_ostatok
# Рекурсивний підбір платежу:
def recurcive_payment_selection(matrix_list, useful_data, params) -> float:
    # Якщо залишок нас влаштовує, то потрібний платіж знайдено
    if ostatok_is_ok(useful_data):
        best = best_ostatok(useful_data['ostatok1'], useful_data['ostatok2'])
        if best == useful_data['ostatok1']:
            if useful_data['min_ostatok'] > 0:
                new_pay = useful_data['pay1'] + 0.01
            else:
                new_pay = useful_data['pay1']
        elif best == useful_data['ostatok2']:
            if useful_data['min_ostatok'] > 0:
                new_pay = useful_data['pay2'] + 0.01
            else:
                new_pay = useful_data['pay2']
        return round(new_pay, 2)
    # Якщо ні - змінюємо платіж і наступна спроба прогнати цикл платежів
    else:
        new_pay = get_changed_payment(useful_data)
        useful_data['pay1'], useful_data['pay2'] = useful_data['pay2'], new_pay
        new_matrix = cycle_payments(matrix_list, useful_data, params)
        new_ostatok = new_matrix[-1]['ostatok']
        renew_useful_data(useful_data, new_pay, new_ostatok)
        return recurcive_payment_selection(matrix_list, useful_data, params)

def main(*kwargs):
    # Отримуємо початкові дані для розрахунку (через get_start_data)
    params = get_start_data(sys.argv[1:])
    # Матриця ключових дат та не заповнених платежів по кредиту
    matrix_list = get_empty_pays_list(params)
    # Дані для подальшого використання:
    useful_data = fill_useful_data(params)
    # Перший примітивний варіант платежу - сумма з усіма відсотками за весь срок кредиту, поділена на срок
    # (в більшості випадків цей платіж більше потрібного):
    useful_data['pay2'] =  primitive_pay(matrix_list, params)
    # Залишок на кінець при використанні цього платежу:
    useful_data['ostatok1']= cycle_payments(matrix_list, useful_data, params)[-1]['ostatok']
    # Заносимо 'pay2' на 'pay1'
    useful_data['pay1'] = useful_data['pay2']
    # Другий примітивний розрахунок платежу: сума кредиту / срок кредиту
    # (в більшості випадків цей платіж менше потрібного):
    useful_data['pay2'] = round(params['Summa'] / params['Srok'], 2)
    # Залишок на кінець при використанні цього платежу:
    useful_data['ostatok2'] = cycle_payments(matrix_list, useful_data, params)[-1]['ostatok']
    # Розраховуємо мінімальні та максимальні залишки та платежі:
    useful_data['min_ostatok'] = min(useful_data['ostatok1'], useful_data['ostatok2'])
    useful_data['max_ostatok'] = max(useful_data['ostatok1'], useful_data['ostatok2'])
    useful_data['min_pay'] = min(useful_data['pay1'], useful_data['pay2'])
    useful_data['max_pay'] = max(useful_data['pay1'], useful_data['pay2'])
    # Цикл підбору планового платежу (рекурсія)
    plan_pay = recurcive_payment_selection(matrix_list, useful_data, params)


    # Друк результатів
    print()
    # Необов'язково, для наочності друкується матриця платежів!!!
    # У випадку дуже великих термінів кредиту, коли погашення відбувається раніше, ніж потрібно...
    # Заповнення матриці платежів з використанням знайденого планового платежу
    # (ця матриця вже не потрібна для пошуку планового платежу, але можливо надалі буде корисною):
    useful_data['pay2'] = plan_pay
    useful_data['end_flag'] = True
    matrix_list = cycle_payments(matrix_list, useful_data, params)
    if matrix_list[-1]['ostatok'] == 0 and matrix_list[-2]['ostatok'] == 0:
        for i in matrix_list:
            print(i)
        print()
        print('Відповідного рішення для такого терміну немає! З підібраною сумою планового платежу погашення кредиту буде достроковим!!!')
    print('Плановий платіж = ', plan_pay)

if __name__=='__main__':
    main()