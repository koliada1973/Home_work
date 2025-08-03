class Bank:
    branches_number = 100000

    def __init__(self, bank_name):
        self.bank_name = bank_name

    def print_attrs(self):
        print(self.bank_name, self.branches_number)


bank1 = Bank('Mega_bank')
bank2 = Bank('Honest_bank')

print(bank1.bank_name)
print(bank2.bank_name)
print(bank1.branches_number)

bank1.print_attrs()
bank2.print_attrs()

bank1.branches_number = 100
bank1.print_attrs()
bank2.print_attrs()