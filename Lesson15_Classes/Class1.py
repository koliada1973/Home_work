class Clients:
    clients_count = 0
    def __init__(self, first_name, middle_name, last_name, old, salary, address='Kyiv', debt=0):
        Clients.clients_count += 1
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.old = old
        self.salary = salary
        self.address = address
        self.debt = debt

    def update_salary(self, new_salary):
        self.salary = new_salary

    def update_debt(self, new_debt):
        self.debt = new_debt

    def print_count_clients(self):
        print("Clients count: ", Clients.clients_count)

    def print_copy_id(self):
        print("Copy ID: ", id(self))

    def compare(self, copy):
        return self.__dict__ == copy.__dict__

a = Clients('Serhii', "Anatoliyovich", 'Koliada', 51, 20000, 'poltava', 0)
print(a.first_name)
a.update_salary(30000)
print(a.salary)
a.print_count_clients()
a.print_copy_id()
print(a.__dict__)


b = Clients('Ivan', 'Serhiyovich', 'Petrov', 45, 15000, 'Sumy', 0)
c = Clients('Ivan', 'Serhiyovich', 'Petrov', 45, 15000, 'Sumy', 0)
print(b.compare(c))