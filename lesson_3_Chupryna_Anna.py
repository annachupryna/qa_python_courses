import random


#Задача 1

number = random.randint(0, 59)
if number <= 15:
    print(f"Число {number} в першій чверті")
elif 15 < number <= 30:
    print(f"Число {number} в другій чверті")
elif 30 < number <= 45:
    print(f"Число {number} в третій чверті")
else:
    print(f"Число {number} в четвертій чверті")

#Задача 2

birth_month = int(input("Введіть місяць свого народження: "))
if birth_month < 0 or birth_month > 12:
    print("Ви вводите некоректні дані. Введіть місяць в форматі числа (без нуля).")
elif 0 < birth_month <= 2:
    print("За вікном падав сніг.")
elif birth_month == 12:
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

# Задача 4.

a = float(input("Enter x: \n"))
b = float(input("Enter y: \n"))

if a == 0:
    if b == 0:
        print("Coordinates 0, 0")
    else:
        print(f"Coordinates 0, {b}")
else:
    if b == 0:
        print(f"Coordinates {a}, 0")
    else:
        if a > 0 and b > 0:
            print("Coordinates belong to I quarter")
        elif a < 0 and b < 0:
            print("Coordinates belong to III quarter")
        elif a > 0 > b:
            print("Coordinates belong to IV quarter")
        else:
            print("Coordinates belong to II quarter")

