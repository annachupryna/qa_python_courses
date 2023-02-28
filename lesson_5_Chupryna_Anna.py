# set, або множина

#пустий сет
set_1 = set()

set_2 = set({1, 45, 8.09, 'abc'})
set_3 = {1, 45, 8.09, 'abc', 'abc', 45}
el = "amm"

if el in set_3:
    print(el)
else:
    print("No el in set")
print(set_3)

# Операція - (мінус) або функція difference()
# Операція обєднання set1 | set2 -> s1.union(s2)
# Перетин множин set1 & set2 -> set1.intersection(set2)
# Симетрична різниця set1 ^ set 2 -> set1.symetric_difference(set2)
# Функція issubset -> s1.issubset(s2)
# Функція issuperset -> s1.issuperset(s2)
# set.len()
# set.copy()
# Як вивести унікальні елементи в списку filteres_set = set(demo_list)
# Чи задана множина є надмножиною над іншою >, >=
# Чи задана множина є підмножиною іншої <, <=
# set.add(el)
# set.remove(el)




