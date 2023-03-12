"""
Homework #1
"""
def user_input():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    d = float(input("Enter d: "))
    return {'a': a, 'b': b, 'c': c, 'd': d}


def figure_definition(a, b, c, d):
    if a == b == c == d:
        diagonal_1 = math.sqrt(a ** 2 + b ** 2)
        diagonal_2 = math.sqrt(c ** 2 + d ** 2)
        if diagonal_1 == diagonal_2:
            print("It is square")
    else:
        def rectangle_square(a, b):
            s = a * b
            print(f"Square of rectangle is {s}")

        diagonal_1 = math.sqrt(a ** 2 + b ** 2)
        diagonal_2 = math.sqrt(c ** 2 + d ** 2)
        if a ** 2 + b ** 2 == c ** 2 + d ** 2 and diagonal_1 == diagonal_2:
            print("It is rectangle")
            rectangle_square(a, b)


figure_sides = user_input()
figure_definition(figure_sides['a'], figure_sides['b'], figure_sides['c'], figure_sides['d'])


"""
Задача 1. Напишіть програму на Python для зведення в квадрат
# і куб кожного числа в заданому списку цілих чисел за допомогою Lambda.
"""
from functools import reduce

# list_1 = [1, 2, 3, 4, 5, 6, 7]
# func_1 = list(map(lambda x: x ** 2, list_1))
# func_2 = list(map(lambda x: x ** 3, list_1))

# print(func_1)
# print(func_2)

"""
Задача 2. Напишіть програму на Python, щоб визначити, чи починається даний рядок 
із заданого символу за допомогою лямбда.
"""

# if_starts_with_letter = lambda symbol, text: True if text.startswith(symbol) else False
# print(if_starts_with_letter("a","abjjjs"))

"""
Напишіть програму Python для підрахунку парних і 
непарних чисел у заданому масиві цілих чисел за допомогою Lambda.
"""

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# filter_even_list = len(list(filter(lambda x: x % 2 == 0, list_1)))
# filter_not_even_list = len(list(filter(lambda x: x % 2 != 0, list_1)))
# print(filter_even_list)
# print(filter_not_even_list)

"""
Напишіть програму на Python для пошуку чисел, які діляться на дев’ятнадцять 
або тринадцять, зі списку чисел за допомогою лямбда.
"""

# list_1 = [13, 26, 39, 456, 450, 87, 19, 38, 57]
# divided_by_digits = list(filter(lambda x: x % 13 == 0 or x % 19 == 0, list_1))
# print(divided_by_digits)

"""
Напишіть програму Python для пошуку паліндромів у заданому списку рядків за допомогою Lambda.
Оригінальний список рядків:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
Список паліндромів:
['php', 'aaa']
"""

# list_1 = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
# is_palindrome = list(filter(lambda x: x == x[::-1], list_1))
# # is_palindrome = list(filter(lambda x: x == x.reverse(), list_1)) - не срабатывает
# print(is_palindrome)