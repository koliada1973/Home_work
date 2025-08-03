# Для задачі 1 додати атрибут класу number=0, і інкрементувати його при створенні кожного екземпляра клієнта.
# Реалізувати вивід (прінт) даного атрибуту, як метод класу.

class Client:
    number = 0
    def __init__(self, full_name, balance):
        self.full_name = full_name
        self._balance = balance
        self.__class__.number += 1

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        self._balance = new_balance

    def del_balance(self):
        del self._balance

    @classmethod
    def inst_count(cls):
        print(f"Number of class instances = {cls.number}")

client1 = Client("John", 100)
client1 = Client("John Connor", 200)

client1.inst_count()


