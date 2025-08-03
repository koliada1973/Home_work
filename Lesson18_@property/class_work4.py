# Ваш клас з задачі 1 почав використовуватись програмістами, що працюють в банку.
# В процесі роботи виявилось, що в ПІБ записуються не коректні дані.
# Прогнозувалось, що ПІБ – це стрінг, в якому знаходяться 3 слова, розділені пробілами, кожне - з великої букви.
# На практиці – туди інколи скидається різна «каша», типу «Петренко В.В», «кум Петро», «Бульба С. – голова колгоспу» і т.д. і т.п.
# Ваша задача – зробити з ПІБ властивість (property), з відповідними операціями (гетер, сетер, делітер),
# для сетера виконати необхідні перевірки, інакше – викидати виключення з описом помилки.

class Client:
    def __init__(self, full_name, balance):
        self._balance = balance
        self.name = full_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance

    @balance.deleter
    def balance(self):
        self._balance = 0

    @property
    def name(self):
        return self.full_name

    @name.setter
    def name(self, full_name):
        self.full_name = full_name.replace('  ', ' ')
        self.full_name = self.full_name.strip(' ')
        list_name = self.full_name.split(' ')
        if len(list_name) == 3:
            for w in list_name:
                if not w[0].isupper():
                    raise ValueError('The first letter is not a title letter!')
            self.full_name = ' '.join(list_name)
        else:
            raise ValueError('Incorrect format!')

    @name.deleter
    def name(self):
        self.full_name = ''

client1 = Client(full_name=' Петренко Василь  Іванович ', balance=5000)
print(client1.name, client1.balance)

client1.name = 'Петренко Василь Степанович'
print(client1.name, client1.balance)

client1.balance = 7000
print(client1.name, client1.balance)

del client1.balance
print(client1.name, client1.balance)

del client1.name
print(client1.name, client1.balance)
