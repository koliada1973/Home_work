# Завдання
# Створи базовий клас Account з:
# приватним атрибутом __balance
# конструктором, що приймає початковий баланс
# методом deposit(amount) — додати суму до балансу
# методом withdraw(amount) — зняти суму, якщо вистачає
# dunder методом __repr__(), що повертає "Account(balance=<balance>)"
# Створи підклас SavingsAccount, який наслідує Account і додає:
# атрибут __interest_rate (приватний)
# метод apply_interest(), що збільшує баланс на відсоток від __interest_rate
# перевизнач метод withdraw(amount), щоб зняти суму лише якщо після зняття баланс не впаде нижче 100 (мінімальний залишок)
# Напиши код, що створює об’єкт SavingsAccount, вносить депозит, знімає гроші, застосовує відсотки і виводить баланс після кожної операції.

class Account:
    def __init__(self, balance):
        self.__balance = balance

    def deposite(self, amount):
        self.__balance += amount
        self.__repr__()

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.__repr__()
        else:
            raise ValueError("Not enough money")

    def __repr__(self):
        return f"Account(balance={self.__balance})"

class SavingsAccount(Account):
    min_balance = 100
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.__interest_rate = interest_rate
        self.apply_interest()

    def apply_interest(self):
        self._Account__balance += self._Account__balance * self.__interest_rate / 100

    def withdraw(self, amount):
        if (self._Account__balance - amount) >= self.min_balance:
            self._Account__balance -= amount
        else:
            raise ValueError("Not enough money")

acc1 = SavingsAccount(10000, 5)
print(acc1)
acc1.withdraw(1000)
print(acc1)
acc1.apply_interest()
print(acc1.__dict__)