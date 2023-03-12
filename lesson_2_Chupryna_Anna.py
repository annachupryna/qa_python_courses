import math

#Завдання 1

first_name = input("Enter your name: ")
surname = (input("Enter your surname: "))

print(f"Student's name is {first_name}, student's surname is {surname}")
print("Student's name is " + first_name + ", student's surname is " + surname)

output_text = "Student's name is " + first_name + ", student's surname is " + surname

print(output_text.lower())
print(output_text.upper())
print(output_text.title())
print(first_name*5)

first_name = "\n\t" + "Anna" + "\t"
print(first_name)

first_name = first_name.strip()
print(first_name)

# Завдання 2

r = (float(input("Enter radius: ")))
c_calculate = (2*math.pi) * r
p_calculate = math.pi * r**2
print(f"Circumference of a circle is {round(c_calculate, 2)}, area of a circle is {round(p_calculate, 1)}")

# Завдання 3

current_dollar_value = float(input("Enter current dollar value: \n"))
hryvnia_input = float(input("How many hryvnias would you like to covert? \n"))
hryvnia_convert_to_dollar = round(float(hryvnia_input / current_dollar_value), 2)
print(f"Current currency course is: {hryvnia_convert_to_dollar} dollars")