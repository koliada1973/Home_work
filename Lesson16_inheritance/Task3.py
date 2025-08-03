# Task 3:
# Магазин товарів
# Напишіть клас Product, який має три атрибути:
# - тип
# - назва
# - ціна.
# Потім створіть клас ProductStore, який матиме декілька Products і працюватиме з усіма товарами в магазині.
# Всі методи, якщо вони не можуть виконати свою дію, повинні згенерувати ValueError з відповідною інформацією про помилку.
# Поради: Під час реалізації класу ProductStore використовуйте концепції агрегації/композиції.
# Ви також можете реалізувати додаткові класи для роботи з певним типом товару тощо.
# Також клас ProductStore повинен мати наступні методи:
# - add(product, amount) - додає вказану кількість одного товару із заздалегідь визначеною для вашого магазину надбавкою до ціни (30 відсотків)
# - set_discount(identifier, percent, identifier_type='name') - додає знижку на всі товари, вказані за допомогою вхідних ідентифікаторів (тип або назва). Знижка має бути вказана у відсотках
# - sell_product(назва_товару, кількість) - видаляє певну кількість товарів з магазину, якщо вони є в наявності, в іншому випадку видає помилку. Також збільшує дохід, якщо метод sell_product спрацював успішно.
# - get_income() - повертає суму доходу, отриманого екземпляром ProductStore.
# - get_all_products() - повертає інформацію про всі доступні товари в магазині.
# - get_product_info(назва_товару) - повертає кортеж з назвою товару та кількістю товарів у магазині.

class Product:
    def __init__(self, prod_type, prod_name, prod_price):
        self.prod_type = prod_type
        self.prod_name = prod_name
        self.prod_price = prod_price

class ProductStore:
    def __init__(self):
        self.price_premium = 30
        self.prod_list = []
        self.income = 0

    def add(self, product, amount):
        product.amount = amount
        product.discount = 0
        product.current_price = product.prod_price * (1 + self.price_premium/100)
        self.prod_list.append(product)

    def set_discount(self, identifier, percent, identifier_type='name'):
        for prod in self.prod_list:
            if identifier_type == 'type':
                if prod.prod_type == identifier:
                    prod.discount += percent
            elif identifier_type == 'name':
                if prod.prod_name == identifier:
                    prod.discount += percent

    def sell_product(self, name, amount):
        ok = False
        for prod in self.prod_list:
            if prod.prod_name == name:
                ok = True
                if prod.amount >= amount:
                    sum_sell = amount * prod.current_price * (1 - prod.discount/100)
                    self.income += sum_sell
                    prod.amount -= amount
                    print(f"Було продано {amount} одиниць товару {prod.prod_name} за ціною {prod.current_price} на суму {sum_sell} (діскаунт {prod.discount}%)!")
                    if prod.amount == 0:
                        self.prod_list.remove(prod)
                elif prod.amount < amount:
                    sum_sell = prod.amount * prod.current_price * (1 - prod.discount/100)
                    self.income += sum_sell
                    print(f"За наявністю було продано лише {prod.amount} одиниць товару {prod.prod_name} за ціною {prod.current_price} на суму {sum_sell} (діскаунт {prod.discount}%)!")
                    self.prod_list.remove(prod)
        print("Цього продукту немає в наявності!") if not ok else None

    def get_income(self):
        return self.income

    def get_all_products(self) :
        print("Список продуктів у продажу:")
        for prod in self.prod_list :
            print(f"{prod.prod_type} | {prod.prod_name} | price={prod.current_price} (old price = {prod.prod_price}) | amount={prod.amount} | discount={prod.discount}%")

    def get_product_info(self):
        pass

product1 = Product('Fruits', 'Apple', 80)
product2 = Product('Fruits', 'Bananas', 100)
product3 = Product('Sport', 'Football T-Shirt', 400)
product4 = Product('Tools', 'hammer', 70)

s = ProductStore()
s.add(product1, 100)
s.add(product2, 200)
s.add(product3, 50)
s.add(product4, 10)
s.get_all_products()
print()

s.set_discount("Fruits", 5, 'type')
s.set_discount("Apple", 5)
s.set_discount("Football T-Shirt", 7)
s.get_all_products()
print()

s.sell_product('Football T-Shirt', 7)
print(f"Прибуток магазину = {s.get_income()}")
s.get_all_products()
print()

s.sell_product('Football T-Shirt', 70)
print(f"Прибуток магазину = {s.get_income()}")
s.get_all_products()
print()

s.sell_product('Apple', 45)
print(f"Прибуток магазину = {s.get_income()}")
s.get_all_products()