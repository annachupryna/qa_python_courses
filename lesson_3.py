

import random


#Задача 1

number = random.randint(0, 59)
if number <= 15:
    print(f"Число {number} в першій чверті")
elif number <= 30:
    print(f"Число {number} в другій чверті")
elif number <= 45:
    print(f"Число {number} в третій чверті")
else:
    print(f"Число {number} в четвертій чверті")

#Задача 2

birth_month = int(input("Введіть місяць свого народження: "))
if birth_month < 0 or birth_month > 12:
    print("Ви вводите некоректні дані. Введіть місяць в форматі числа (без нуля).")
elif 0 < birth_month <= 2 or birth_month == 12:
    print("За вікном падав сніг.")
elif 6 > birth_month >= 3:
    print("Все довкола розцвітало.")
elif 9 > birth_month >= 6:
    print("Діти насолоджувались літніми канікулами.")
else:
    print("Все довкола загоралось яскравими фарбами.")

#Задача 3

number = int(random.randint(0, 999))
last_digit = number % 10

if last_digit % 2 == 0:
    a1 = number % 10
    a2 = number // 10
    a3 = a2 % 10
    a4 = a2 // 10
    if (a1 + a3 + a4) % 3 == 0:
        print(f"{number} ділиться на 6")
    else:
        print(f"{number} не ділиться на 6")
else:
    print(f"{number} не ділиться на 6")

#Задача 4

x = float(input("Enter x: \n"))
y = float(input("Enter y: \n"))

if x == 0:
    if y == 0:
        print("Coordinates 0, 0")
    else:
        print(f"Coordinates 0, {y}")
else:
    if y == 0:
        print(f"Coordinates {x}, 0")
    else:
        if x > 0 and y > 0:
            print("Coordinates belong to I quarter")
        elif x < 0 and y < 0:
            print("Coordinates belong to III quarter")
        elif x > 0 > y:
            print("Coordinates belong to IV quarter")
        else:
            print("Coordinates belong to II quarter")