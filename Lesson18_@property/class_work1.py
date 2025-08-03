# Створити клас клієнта банку, який приймає атрибути:
# ·      ПІБ
# ·      баланс рахунку (захищений атрибут)
# Реалізувати методи (звичайні, не property), які б дозволили:
# ·      отримувати баланс
# ·      присвоювати баланс
# ·      видаляти атрибут баланс
# Створити екземпляр класу, відпрацювати всі методи.

class Client:
    def __init__(self, full_name, balance):
        self.full_name = full_name
        self._balance = balance

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        self._balance = new_balance

    def del_balance(self):
        del self._balance

client1 = Client("John", 100)
print(client1.get_balance())
client1.set_balance(5000)
print(client1.get_balance())
# client1.del_balance()
# print(client1.get_balance())