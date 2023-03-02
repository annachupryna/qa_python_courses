# Задача 1 по дефолту друкує в порядку зростання??

list_1 = [67, 4, 6, 7, 3, 11, 9, 45, 56, 56, 50]
list_2 = [3, 4, 55, 7, 45, 11, 9, 45, 56, 67, 56, 50]

list_intersection = list(set(list_1).intersection(set(list_2)))
print(sorted(list_intersection))

# Задача 2
students_score = {
    'Petro': 12,
    'Ivan': 9,
    'Olena': 6
}

average = sum(students_score.values())/len(students_score)

for student in students_score.keys():
    if students_score[student] > average:
        print(student)

# Задача 3
number_list = [1, 1, 3, 3, 4, 1, 1, 2, 3, 4, 4, 4, 5, 6, 8, 9, 7, 7, 6, 5]
value_count = len(set(number_list))
print(value_count)

# Задача 4
list_1 = list(input("Enter your first list:"))
list_1_set = set(list_1)
list_2 = list(input("Enter your second list:"))
list_2_set = set(list_2)
common_numbers = sorted(list(list_1_set.intersection(list_2_set)))
print(f"Common numbers for both lists are: {common_numbers}")

print("Below is list_1")
for el in sorted(list_1):
    print(el)

print("Below is list_2")
for el in sorted(list_2):
    print(el)

# Задача 5
words_string = "one two three one four five seven ten seven one"
#words_list повертає список
words_list = words_string.split()
word_dictionary = {}

for el in words_list:
    if el in word_dictionary:
        word_dictionary[el] = word_dictionary[el] +1
    else:
        word_dictionary[el] = 1

print(set(word_dictionary.items()))




