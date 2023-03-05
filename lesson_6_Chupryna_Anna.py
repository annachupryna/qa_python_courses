#
# num_1 = int(input("Enter num_1: "))
# num_2 = int(input("Enter num_3: "))
# user_action = input("Enter your action: ")
#
#
# def add(num1, num2) -> int:
#     return num1 + num2
#
#
# def minus(num1, num2) -> int:
#     return num1 - num2
#
#
# def multiply(num1, num2) -> int:
#     return num1 * num2
#
#
# def division(num1, num2) -> int:
#     return num1 / num2
#
#
# if user_action == "add":
#     print(add(num_1, num_2))
# elif user_action == "minus":
#     print(minus(num_1, num_2))
# elif user_action == "multiply":
#     print(multiply(num_1, num_2))
# elif user_action == "division":
#     print(division(num_1, num_2))
# else:
#     user_action = input("Enter valid action:")


def isInRange(to, value, from1=0) -> bool:
    if to >= value >= from1:
        return True
    return False


print(isInRange(7, 5))