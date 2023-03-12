import math
import string
import random
from functools import reduce

# ДЗ додаткове завдання 1. Напишіть програму для знаходження перетину двох заданих масивів за допомогою лямбда.

list_1 = [1, 2, 3, 4, 5, 6, 7]
list_2 = [4, 5, 6, 7, 8, 9, 10]
list_intersection = list(filter(lambda x: x in list_1, list_2))
# list_intersection = list(lambda x, y: x.intersection(y), list_1, list_2)
print(list_intersection)

# ДЗ додаткове завдання 2. Напишіть програму на Python, щоб перевірити, чи є заданий рядок числом, за допомогою лямбда

str_1 = "9987"
is_digit = lambda x: x.isdigit()
if is_digit(str_1):
    print('is digit')
else:
    print('not a digit')

# ДЗ додаткове завдання 3. Напишіть програму, щоб знайти список із макс та мін довжиною за допомогою лямбда.

list_1 = [[1, 45], [56, 1, 4], [21, 41, 54, 1]]
min_el = reduce(lambda x, y: x if len(x) < len(y) else y, list_1)
print(f"List with minimum number of elements: {min_el}")
max_el = reduce(lambda x, y: x if len(x) > len(y) else y, list_1)
print(f"List with maximum number of elements: {max_el}")

# ДЗ додаткове завдання 4. Напишіть програму на Python для обчислення добутку заданого списку чисел за допомогою лямбда.
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_multiply = reduce(lambda x, y: x * y, num_list)
print(list_multiply)

"""
ДЗ Основна задача 1
"""


def user_input():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    d = float(input("Enter d: "))
    return {'a': a, 'b': b, 'c': c, 'd': d}


def figure_definition(a, b, c, d):
    def is_square(a, b, c, d):
        return a == b == c == d

    diagonal = math.sqrt(a ** 2 + b ** 2)
    if round(diagonal ** 2, 1) == a ** 2 + b ** 2:
        if is_square(a, b, c, d):
            print("It is square")
        else:
            def rectangle_square(a, b):
                s = a * b
                print(f"Square of rectangle is {s}")

            if a ** 2 + b ** 2 == c ** 2 + d ** 2:
                print("It is rectangle")
                rectangle_square(a, b)
            else:
                print("Введені данні не відповідають параметрам опуклого чотирикутника")


figure_sides = user_input()
figure_definition(figure_sides['a'], figure_sides['b'], figure_sides['c'], figure_sides['d'])


"""
ДЗ Основна задача 2
"""


names = ["anna", "ivan", "maryna", "oleh", "anastasiia", "dmytro"]
domains = ["com", "net", "edu", "org", "gov", "mil"]


def create_email(names, domains):
    def generate_random_num():
        random_num = str(random.randint(100, 999))
        return random_num

    def generate_random_string():
        length = random.randint(5, 7)
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def rand_i(list_of_elements):
        i = random.randrange(len(list_of_elements))
        return i

    generated_email = (names[rand_i(names)] + "." +
                       generate_random_num() + "@" +
                       generate_random_string() + "." +
                       domains[rand_i(domains)])
    print(generated_email)
    return generated_email


create_email(names, domains)
