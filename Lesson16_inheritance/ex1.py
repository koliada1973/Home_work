# Задача 1.
#  Створити клас клієнта, з атрибутами:
# ·      ПІБ
# ·      Дата народження (на вхід подається str в форматі ‘yyyy-mm-dd’, проте зберігається лише рік ‘yyyy’ )
# ·      залишок на рахунку
# ·      місто проживання
# Створити підклас VIP-клієнта, додати дані:
# ·      дата народження (на вхід подається str в форматі ‘yyyy-mm-dd’, в такому ж вигляді і зберігається)
# ·      рівень VIP (можливі значення від 1 до 5)
# Для VIP – клієнта створити методи:
# ·      зміни рівня VIP
# ·      __repr__ та __str__, в яких виведіть всі поля, але для __repr__ виведіть ще тип поля. Потестуйте ці методи після кожного з 3-х варіантів ініціалізації екземпляра, що вказані нижче.
# ·      1-ий варіант ініціалізації, з використанням аналогічного методу батьківського класу
# ·      2-ий варіант ініціалізації, написати свій метод (і зрозуміти, чому зручніше використовувати батьківський :) )
# ·      3-ий варіант ініціалізації, коли спочатку присвоюються атрибути специфічні для VIP, а потім викликається super(). Всі значення атрибутів коректні ? Дата народження, нап ?

class Clients:
    def __init__(self, full_name, birth_date, remain, address):
        self.full_name = full_name
        self.birth_date = birth_date[:4]
        self.remain = remain
        self.address = address

class Vip_clients(Clients):
    def __init__(self, full_name, birth_date, remain, address, level):
        # super().__init__(full_name, birth_date, remain, address)
        Clients.__init__(self, full_name, birth_date, remain, address)
        self.birth_date = birth_date
        self.level = level


    def change_level(self, level):
        self.level = level

    def __str__(self):
        return f"str = {self.full_name} {self.birth_date} {self.remain} {self.address} {self.level}"

    def __repr__(self):
        return (f"repr = {self.full_name} ({type(self.full_name)})  {self.birth_date} ({type(self.birth_date)}) {self.remain} ({type(self.remain)})  {self.address} ({type(self.address)}) {self.level} ({type(self.level)}) ")

client1 = Vip_clients('Ivan Petroenko', "1984-10-25", 10000, "Kiyv", 2)
print(client1)
print(client1.__repr__())
print(repr(client1))
client1.change_level(10)
print(client1.remain)

