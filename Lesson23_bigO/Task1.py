# Task 1:
# Зіставте складність великих О з фрагментами коду нижче
# Припустимо, що всі списки, які передаються у функції, мають однакову довжину N
# answers
# 1 - log n
# 2 - n^2
# 3 - n
# 4 - n^2
# 5 - 1
# 6 - n

from typing import List, Tuple

# answer 3 - n
# - залежність лінійна, тому що кожний елемент одного списку буде перевірено, чи є він в іншому списку
# (хоча тут питання: чи не є перевірка входження елементу в список теж прихованим циклом)
def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res

# answer 5 - 1
# - залежність постійна, тому що кількість проходів циклу є константою (=10)
def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n

# answer 2 - n^2 - залежність квадратична,
# тому що кожен елемент одного списку буде перевірено з кожним елементом іншого списке (цикл в циклі):
def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp

# answer 6 - O(n) - залежність лінійна, тому що кожен елемент списку буде перевірено в циклі:
def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res

# answer 4 - n^2
# - залежність квадратична, тому що кількість кроків буде дорівнювати кількости проходжень циклу в середині іншого циклу (цикл в циклі):
def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res

# answer 1 - O(log n)
# - залежність логарифмічна (кількість кроків буде зменьшуватись, у результаті кількість кроків буде меньше ніж n):
def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n