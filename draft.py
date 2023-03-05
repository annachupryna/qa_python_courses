# from collections import Counter
#
# """
# set, або множина
# """
#
#
# #пустий сет
# set_1 = set()
#
# set_2 = set({1, 45, 8.09, 'abc'})
# set_3 = {1, 45, 8.09, 'abc', 'abc', 45}
# el = "amm"
#
# if el in set_3:
#     print(el)
# else:
#     print("No el in set")
# print(set_3)
#
# # Операція - (мінус) або функція difference()
# # Операція обєднання set1 | set2 -> s1.union(s2)
# # Перетин множин set1 & set2 -> set1.intersection(set2)
# # Симетрична різниця set1 ^ set 2 -> set1.symetric_difference(set2)
# # Функція issubset -> s1.issubset(s2)
# # Функція issuperset -> s1.issuperset(s2)
# # set.len()
# # set.copy()
# # Як вивести унікальні елементи в списку filteres_set = set(demo_list)
# # Чи задана множина є надмножиною над іншою >, >=
# # Чи задана множина є підмножиною іншої <, <=
# # set.add(el)
# # set.remove(el) - буде помилка якщо відсутній
# # set.discard(el) - не буде помилка якщо відсутній
# # set.pop() - витягує рандомний елемент і повертає його, в сеті його вже не буде
#
#
#
# """
# Словники , dictionary
# має пару {key: value}
# доступ виконується за ключем
# невпорядкована
# змінна (можна змінити лише значення, а ключ - ні)
# списки словники не можуть бути ключами ???
# """
# dict_1 = {}
# # 1 - key, Monday - value
# dict_1 = {1: "Monday", 2: "Tuesday", 3: "Wednesday"}
#
# # звернення за індексом. за 1 індексом виводить 1 елемент (але індекс рахується з нуля?)
# print(dict_1[1])
# print(dict_1)
#
# # 1 Monday - key, 1 - value
# dict_2 = dict(Monday=1, Tuesday=2, Wednesday=3)
# print(dict_2)
#
# # 1 - key, Monday - value
# dict_3 = dict({1: "Mon", 2: "Tues", 3: "Wed"})
# print(dict_3)
# dict_3[6] = "Saturday"
# print(dict_3)
#
# # dict_1.update(dict_2) - обєднання словників, змінює поточний словник
# print(f"це dict_1 до змін {dict_1}")
# print(dict_3)
# dict_1.update(dict_3)
# print(f"це dict_1 {dict_1}")
#
# # del
# dict_3.pop(2)
# del dict_1[1]
# print(dict_1)
# # clear()
# dict_3.clear()
# dict_3 = {}
#
# # get() - отримуємо значення зі словника, якщо значення немає - записує
# print(dict_1.get(2))
# # повертає, але не записує
# print(dict_1.get(7, "Sunday"))
# print(dict_1)
#
# # як достучатись до вкладених значень
# hierarchical_dict = {
#     1: {
#         "key1": {
#             "key2": "value2"
#         }
#     },
#     2: "value2"
# }
# print(hierarchical_dict[1]['key1']['key2'])
# print(hierarchical_dict.get(1).get('key1').get('key2'))
#
# #dict.keys() - звертаємось до ключів
# print(dict_1.keys())
# print(list(dict_1.keys()))
#
# # dict.values() - звертаємось до значень
# print(dict_1.values())
#
# #dict.items() - звертаємось до значень і ключів, повертає кортеж
# print(dict_1.items())
# print(list(dict_1.items()))
#
# # dict.setdefault(key, value) - функція яка створює елемент словника з ключем якщо заданий ключ відсутній
# # якщо ключ існує - нічого не зміниться якщо ні - додасться новий
# dict_1.setdefault(5, "Friday")
# print(dict_1)
#
# # проходження по словнику
# for el in dict_1.keys():
#     print(el)
#
# for key, value in dict_1.items():
#     print(key, value)
#
# # поветає кортеж
# for el in dict_1.items():
#     print(el)
#
# # zip() - функція створює словник шляхом обєднання списку ключів і списку значень
# # обовязково огорнути в dict
# key_list = [1, 2, 3, 4]
# value_list = ["Mon", "Tue", "Wed", "Thur"]
# new_dictionary = dict(zip(key_list, value_list))
# print(new_dictionary)
#
# # як можна сортувати словник не дефолтним методом
# from collections import OrderedDict
# sorted_dict = OrderedDict(sorted(new_dictionary.items()))
# print(sorted_dict)
#
# #result = {10, 30}
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# result = set1.difference(set2)
# print(result)
#
# #Задача 1 оголошуємо словник
# student_dict = {
#     "Ivan": 10,
#     "Olena": 15,
#     "Petro": 8,
#     "Maryna": 13
# }
# # визначаємо середній бал студентів
# #student_marks = list(student_dict.values())
# marks_sum = 0
# for value in student_dict.values():
#     marks_sum += value
# #можна плюсувати значення словника без приведення їх до інт
# # print(type(student_dict.values()))
# # print(sum(student_dict.values()))
# average_mark = marks_sum / len(student_dict)
# print(average_mark)
# # звертаємося до кожного ключа в словнику
# for student in student_dict.keys():
#     # за індексом виводиться значення
#     # якщо value кожного ключа за індексом більше
#     if student_dict[student] > average_mark:
#         print(student)
#
# #Задача 1 рішення 1
# # names_dict = {
# #     1: "Maria",
# #     2: "Ivan",
# #     3: "Ovena"
# # }
# # user_input = int(input("Enter your id: "))
# # for user_input in names_dict.keys():
# #     print(f"hello {names_dict[user_input]}")
# #     user_input = int(input("Enter your id: "))
# # рішення 2
# # names_dict = {
# #     1: "Maria",
# #     2: "Ivan",
# #     3: "Ovena"
# # }
# #
# # user_input = int(input("Enter your id: "))
# # if user_input in names_dict:
# #     print(names_dict[user_input])
# # else:
# #     print("hello all")
# # рішення 3
# # names_dict = {
# #     1: "Maria",
# #     2: "Ivan",
# #     3: "Ovena"
# # }
# # user_input = int(input("Enter your id: "))
# # print(f"hello {names_dict.get(user_input, 'all')}")

# Отсортируйте словарь по значению в порядке возрастания и убывания.
# dict_1 = {"Maria": 1,
#           "Ivan": 10,
#           "Olena": 4,
#           "Lolo": 45,
#           "Ui": 6
# }
# dict_1_copy = sorted(dict_1.values())
# print(dict_1_copy)
# sorted_dict = {}
# # для каждого элемента с списке значений
# for el in dict_1_copy:
#     # для каждого ключа в словаре
#     for key in dict_1.keys():
#         # сравниваем равно ли значение по ключу в словаре элементу
#         if dict_1[key] == el:
#             sorted_dict[key] = dict_1[key]
# print(sorted_dict)
#
# dict_1_copy = sorted(dict_1.values(), reverse=True)
# print(dict_1_copy)
# sorted_dict = {}
# # для каждого элемента с списке значений
# for el in dict_1_copy:
#     # для каждого ключа в словаре
#     for key in dict_1.keys():
#         # сравниваем равно ли значение по ключу в словаре элементу
#         if dict_1[key] == el:
#             sorted_dict[key] = dict_1[key]
# print(sorted_dict)

# list1=[2,4,6,8,10]
# print(list1[-2])
#
# list2 = [17,23,41,10]
# list2.append(32)
# print(list2)
#
# setA={3,6,9}
# setB={1,3,9}
# print(setA|setB)
#
# a=[1,2,3,4,5,6,7,8,9]
#
# print(a[::2])
# a=[1,2,3,4,5,6,7,8,9]
# arr = [[1, 2, 3, 4],
# [4, 5, 6, 7],
# [8, 9, 10, 11],
# [12, 13, 14, 15]]
# for i in range(0, 4):
#     print(arr[i].pop())
#
# print(a[::2])
# init_tuple = (1,) * 3
#
# init_tuple[0] = 2
#
# print(init_tuple)
# init_tuple = ((1, 2),) * 7
# print(len(init_tuple[3:8]))

# a = {(1,2):1,(2,3):2}
# print(a[1,2])

# a = {'a':1,'b':2,'c':3}
# print (a['a','b'])

# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# sum = 0
# for k in arr:
#     sum += arr[k]
# print (sum)
# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12
sum = 0
for k in my_dict:
    sum += my_dict[k]
print (sum)
print(my_dict)