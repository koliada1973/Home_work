# Напишіть функцію з ім'ям "choose_func", яка отримує список чисел і 2 функції зворотного виклику.
# Якщо всі числа у списку додатні, виконати першу функцію зі списку і повернути її результат.
# В іншому випадку поверніть результат другої функції

def choose_func(nums: list, func1, func2):
    new_list = [i for i in nums if i > 0]
    if new_list == nums:
        print(f'В списку {nums} всі числа додатні, виконуємо першу функцію над списком та повертаємо її результат...')
        return func1(nums)
    else:
        print(f'В списку {nums} не всі числа додатні, виконуємо другу функцію над списком та повертаємо її результат...')
        return func2(new_list)

# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25], 'Умова assert 1 не виконується...'
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5], 'Умова assert 2 не виконується...'