# Task_2:

# Перебираємо в циклі кожну пару з словника stock: назву товару (product_name) і його кількість (quantity)
# Знаходимо відповідну ціну товару в словнику prices за назвою (ключ = product_name)
# Обчислюємо вартість товару (price * quantity) і додаємо цю вартість до total_price

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = 0

for product_name, quantity  in stock.items():
    total_price += prices[product_name] * quantity

print('Task 2:')
print(f'Загальна ціна товарів: {total_price}')