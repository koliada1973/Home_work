# Створити клас клієнта (Client),
# ·      атрибути:
# ◦  ПІБ
# ◦  дата народження (string)
# ·      методи:
# ◦  __init__ (приймає ПІБ, дату народження),
# ◦  вивести інформацію про клієнта (ПІБ, дату народження)
# Створити клас Рахунок (Account):
# ·      атрибути:
# ·      клієнт (екземпляр класу Client)
# ·      залишок на рахунку (захищений атрибут !)
#            методи:
# ·      __init__ (приймає екземпляр класу Клієнт, залишок на рахунку встановлює 0)
# ◦  змінити залишок на рахунку (приймає від“ємне або додатнє число) (захищений метод !)
# ◦  вивести залишок на рахунку
# Створити клас gold-Рахунок (GoldAccount, наслідує Account):
# ·      метод виводу залишку на рахунку та метод зміни залишку на рахунку зробити приватними.
# Потрібно:
# ·      Створити екземпляр кожного з класу, спробувати виконати всі методи.
# ·      здійснити доступ до атрибутів та методів кожного екземпляра (додавши нові методи):
# ◦  з свого класу
# ◦  з класу , що наслідується
# ◦  з основної програми.
#  Чи вірні наступні припущення:
# :black_small_square:  захищені методи доступні зі свого класу, з класу що наслідується, та з основної програми
# приватні методи доступні зі свого класу, але закриті для доступу з класу що наслідується, та з основної програми. Проте до них можна добратись через нотацію _{origin Class}__method | attr
#  Тобто додати нову функціональність (методи)перевіряти методи та атрибути можна з допомогою __dict__, dir() (edited)

class Client:
    def __init__(self, full_name, birthday):
        self.full_name = full_name
        self.birthday = birthday

    def get_info(self):
        print(f"Ім'я клієнта: {self.full_name} ({self.birthday})")

class Account:
    def __init__(self, client: Client):
        self.client = client
        self._remain = 0

    def _change_remain(self, ch_remain):
        self._remain += ch_remain

    def show_remain(self):
        print(f"Залишок на рахунку {self.client.full_name}: {self._remain}")

class GoldAccount(Account):
    def __change_remain(self, ch_remain):
        self._remain += ch_remain

    def __show_remain(self):
        print(f"Залишок на рахунку {self.client.full_name}: {self._remain}")

    def secret_method(self):
        return self.__show_remain()

class PlatinumAccount(GoldAccount):
    def show_secret(self):
        return self.__show_remain()


cl1 = Client("Іванов Петро", "01.01.2001")
cl2 = Client("Оля Весела", "11.10.1990")
cl3 = Client("Вася Красивий", "22.05.1980")

acc1 = Account(cl1)
acc1._change_remain(10000)
acc1.show_remain()

acc2 = GoldAccount(cl2)
# acc2._GoldAccount__change_remain(30000)
# acc2._GoldAccount__show_remain()
acc2.secret_method()

acc3 = PlatinumAccount(cl3)
acc3._change_remain(5000)
acc3.show_remain()