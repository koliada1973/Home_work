from datetime import datetime, timedelta, date
import re

# Розпізнавання дати з тексту:
def parse_date(s: str) -> date:
    """
    Розпізнає дату у різних форматах (включаючи українські назви місяців)
    """
    # Невелика підготовка: заміна символів на "/" (найбільше шаблонів з "/")
    s = s.strip().lower()
    s = s.replace("-", "/")
    s = s.replace("*", "/")
    s = s.replace("+", "/")
    s = s.replace(",", "/")
    s = s.replace(".", "/")
    # Українські місяці
    months_ua = {
        "січня": 1, "лютого": 2, "березня": 3, "квітня": 4, "травня": 5,"червня": 6,
        "липня": 7, "серпня": 8, "вересня": 9, "жовтня": 10, "листопада": 11, "грудня": 12}
    # 1. Перевірка формату "5 липня 2025"
    for month_name, month_num in months_ua.items():
        if month_name in s:
            try:
                parts = s.replace("/", "").split()
                day = int(parts[0])
                year = int(parts[-1])
                if year < 100:  # Короткий рік (25 → 2025)
                    year += 2000 if year < 50 else 1900 # Тернарний оператор!
                return date(year, month_num, day)
            except Exception:
                continue
        # 1.2 Перевірка формату типу "5.8", тобто краткої форми запису "05.08.2025"
        elif str(month_num) in s and len(s) < 6:
            try:
                parts = s.split("/")
                day = int(parts[0])
                month_num = int(parts[1])
                if len(parts) == 3:
                    year = int(parts[2])
                else:
                    if month_num < datetime.today().month:
                        year = datetime.today().year + 1
                    else:
                        year = datetime.today().year
                return date(year, month_num, day)
            except Exception:
                continue
    # 2. Популярні шаблони
    patterns = [
        "%d.%m.%Y", "%d/%m/%Y", "%Y-%m-%d",
        "%d.%m.%y", "%d/%m/%y", "%Y/%m/%d", "%y/%m/%d",
        "%m/%d/%Y", "%b %d, %Y", "%B %d, %Y",
    ]
    for p in patterns:
        try:
            dt = datetime.strptime(s, p)
            return dt.date()
        except ValueError:
            continue
    # 3. Шукаємо дату в рядку (типу "приблизно 05.07.25")
    match = re.search(r"(\d{1,2})[.\-/](\d{1,2})[.\-/](\d{2,4})", s)
    if match:
        d, m, y = map(int, match.groups())
        if y < 100:
            y += 2000 if y < 50 else 1900
        return date(y, m, d)
    # raise ValueError(f"Не вдалося розпізнати дату: «{s}»")

# Перетворення дати в рядок тексту заданого формату:
def format_date_ua(d: date, format_string="dd.mm.yyyy") -> str:
    """
    Форматує дату в заданий формат з українськими місяцями:
    Можна задавати формати з шаблонів:
        dd – день з нулем (01)
        d – день без нуля (1)
        mm – місяць з нулем (08)
        m – місяць без нуля (8)
        yyyy – повний рік (2025)
        yy – короткий рік (25)
        MMMM – повна назва місяця українською (серпня)
        MMM – коротка назва місяця українською (сер)
    Наприклад:
        print(format_date_ua(today, "dd.mm.yyyy"))    # 01.08.2025
        print(format_date_ua(today, "d MMMM yyyy"))   # 1 серпня 2025
        print(format_date_ua(today, "yyyy/MM/dd"))    # 2025/08/01
        print(format_date_ua(today, "d MMM yy"))      # 1 сер 25
    """
    # Словники українських назв
    months_full = [
        "", "січня", "лютого", "березня", "квітня", "травня","червня", "липня", "серпня", "вересня", "жовтня", "листопада", "грудня"]
    months_short = [
        "", "січ", "лют", "бер", "кві", "трав","чер", "лип", "сер", "вер", "жов", "лис", "гру", "січн", "берез", "квіт", "травн","черв", "липн", "серп", "верес", "жовт", "лист", "груд"]
    # Замінюємо шаблони
    result = format_string
    result = result.replace("dd", f"{d.day:02d}")   # день з нулем
    result = result.replace("d", f"{d.day}")        # день без нуля
    result = result.replace("mm", f"{d.month:02d}") # місяць з нулем
    result = result.replace("m", f"{d.month}")      # місяць без нуля
    result = result.replace("yyyy", f"{d.year}")    # рік 4 цифри
    result = result.replace("yy", f"{d.year%100:02d}")  # рік 2 цифри
    result = result.replace("MMMM", months_full[d.month])  # повна назва місяця
    result = result.replace("MMM", months_short[d.month])  # коротка назва місяця
    return result

# Отримання від користувача дати першої оплати у випадку
# коли між датою відкриття договору та датою першої оплати - всього кілька днів:
def ask_user_first_pay_date(date1: date, date2: date, delta_days = 10) -> date:
    """Якщо допустити випадок, коли договір відкривається в останні дні місяця (наприклад, 31 числа),
        а перша оплата за умовами договору має бути в перші дні місяця (наприклад 1 числа), то може скластися ситуація
        коли перша оплата має бути буквально на наступний день; або через кілька днів від моменту відкриття договору.
        Тому є сенс в таких випадках пропонувати клієнту змістити дату першої оплати на пізнішу дату....
        Якщо наступна дата відстоїть від початкової менше ніж на дозволену кількість днів (10 днів за замовчанням),
        то користувачу пропонується 3 варіанти вибрати дати першої оплати:
        1) в наступному місяці,
        2) через місяць,
        3) ввести дату вручну.
    """
    pay_date = format_date_ua(date1, "dd.mm.yyyy")
    alt_pay_date = format_date_ua(date2, "dd.mm.yyyy")
    text = f"""    {pay_date} - натисніть 0
    {alt_pay_date} - натисніть 1 
    Або введіть свій варіант дати першої оплати ---> """
    while True:
        user_answer = input(text)
        if user_answer == '0' or user_answer == '1':
            if user_answer == '0':
                result = date1
                break
            elif user_answer == '1':
                result = date2
                break
        else:
            result = parse_date(user_answer)
            if result == None:
                text = f'Помилка визначення дати!\n {pay_date} -0; {alt_pay_date} -1; свій варіант: --> '
                continue
            elif result < date1:
                text = f'Визначена дата {result} раніше дати створення договору!\n {pay_date} -0; {alt_pay_date} -1; свій варіант: --> '
                continue
            else:
                break
    return result

# Розрахунок дати, віддаленої від початкової на N місяців (1 місяць за замовчанням):
def add_months(date1: date, day_of_pay: int, months=1) -> date:
    """
    Додає до дати задану кількість місяців з урахуванням потрібного дня місяця
    """
    # Обчислюємо новий рік і місяць
    month = date1.month - 1 + months
    year = date1.year + month // 12
    month = month % 12 + 1
    # Визначаємо останній день нового місяця
    day = min(day_of_pay, [31,
                            29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28,
                            31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
    return date1.replace(year=year, month=month, day=day)

# Декоратор функції add_months для отримання дати першої оплати:
from functools import wraps
def first_pay_decorator(func, date1, day_of_pay, allowable_days=10):
    """У випадку дати першої оплати вона розраховується як і всі інші дати - додаванням місяця до попередньої дати,
    але коли від відкриття договору до першої оплати проходить меньше певної кількості днів (меньше 10 днів) -
    потрібно порадитись з користувачем..."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Тимчасова дата як дата date1 в яку підставляється day_of_pay
        temp_date = date(date1.year, date1.month, day_of_pay)
        # Застосовуємо функцію add_months для отримання дати першої оплати (через 1 місяць):
        first_pay_date = func(temp_date, day_of_pay)
        # Різниця між старт-датою (дата договору) та датою першої оплати:
        delta_days = first_pay_date - date1
        if delta_days.days <= allowable_days:
            print(f'Дата першої оплати лише через {delta_days.days} днів після відкриття договору, тому потрібно зробити вибір:')
            # Застосовуємо функцію add_months для отримання альтернативної дати першої оплати (через 2 місяці):
            alt_first_pay_date = func(temp_date, day_of_pay, 2)
            # Застосовуємо функцію user_first_pay_date для вирішення з користувачем яку дату приймати за дату першої оплати:
            return ask_user_first_pay_date(first_pay_date, alt_first_pay_date, delta_days.days)
        else:
            return first_pay_date
    return wrapper