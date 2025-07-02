from timeit import timeit

# 1. Викорстовуючи map, отримайте значення в кубі (x**3) для значень 0, 1, 2, 3
def f_cubic(num):
    return num ** 3
nums = [0, 1, 2, 3]
result = list(map(f_cubic, nums))
print(result)

# 2. Вирішіть цю саму задачу, використовуючи генератор списку
result = [f_cubic(i) for i in nums]
print(result)

# 3. Використайте timeit.timeit щоб виміряти, який з підходів працює швидше (порівнюйте map-об“єкт і список)
print('Time f_cubic: ', timeit(stmt='[f_cubic(i) for i in nums]', number=100000, globals= {'f_cubic': f_cubic, 'nums': nums}))
print('Time map(f_cubic, nums): ', timeit(stmt='map(f_cubic, nums)', number=100000, globals= {'f_cubic': f_cubic, 'nums': nums}))

# 4. Використайте sys.getsizeof щоб виміряти об’єм пам’яті, що займають об’єкти (порівнюйте map-об“єкт і список)
import sys
print(sys.getsizeof([f_cubic(i) for i in nums]))
print(sys.getsizeof(map(f_cubic, nums)))

# 5. З допомогою random згенеруйте список з 20 елементів, що містить значення в діапазоні від 1 до 50.
# Використовуючи функції  filter() та lambda, відфільтруйте значення, кратні 3.
import random
nums = [random.randint(1, 50) for i in range(20)]
print(nums)
x = list(filter(lambda x: x % 3 == 0, nums))
print(x)

# 6. З допомогою random згенеруйте 2 списки з випадковими числами, в одному 5 елементів, в іншому 10.
# - З допомогою zip отримайте результуючий список
# - з допомогою zip_longest отримайте результуючий список, відсутні значення замініть „err“
from itertools import zip_longest

rand_list1 = [random.randint(1, 50) for i in range(5)]
rand_list2 = [random.randint(1, 50) for i in range(10)]
print('rand_list1: ', rand_list1)
print('rand_list2: ', rand_list2)

result = list(zip(rand_list1, rand_list2))
print('result zip: ', result)

result2 = list(zip_longest(rand_list1, rand_list2, fillvalue='err'))
print('result zip_longest: ', result2)

# 7. Згенерувати рандомний список з 5 елементів (діапазон від 1 до 10).
# При допомозі функцій reduce() та lambda реалізуйте наступний алгоритм: ((((1 * 2) + 3) * 4) * 5)
# (для допомоги дивись опис функції,  help(reduce))
from functools import reduce

ns = [random.randint(1, 10) for i in range(5)]
print('ns: ', ns)
result = reduce(lambda x, y: x + y, ns)
print(result)

# 8. Реалізуйте функцію f_val для розрахунку об’єму прямокутного паралелепіпеду,
# яка приймає на вхід параметри (висота, ширина, глибина; в метрах).
# З допомогою ф-ії partial переробіть f_val таким чином,
# щоб розраховувася об“єм для висоти 1 метр.
from functools import partial
def f_val(width, depth, height):
    return height * width * depth
volume_1metr = partial(f_val, height = 1)
print('volume 1metr*2metr*3metr: ', volume_1metr(width = 2, depth = 3))
print('volume 1metr*5metr*3metr: ', volume_1metr(5, 3))

# Цікавий момент:
# Якщо height оголосити у функції як перший параметр,
# то width та depth потрібно прописувати поіменно,
# а якщо height оголосити у функції як останній параметр,
# то width та depth можна задати як позиційні аргументи..