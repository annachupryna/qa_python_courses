"""
Це програма для введення та перегляду нотаток, які створює користувач.
Програма пропонує юзеру вводити одне із шести ключових слів відповідно до якого відбувається дія.
"""
print("We are happy to welcome you in our notes app.")
notes_list = []
user_input = input("Please, enter your action: ")

# Програма опрацьовує будь-яку дію юзера якщо це не ключовее слово "Exit" (з великої літери відпоідно до умов).
while user_input != "Exit":

    # Програма пропонує ввести юзеру нотатку та додає її в список notes_list[].
    if user_input == "add":
        add_input = input("Enter the note you want to add: ")
        notes_list.append(add_input)
        print(notes_list)
        user_input = input("Please, enter your action: ")

    # Програма сортує та виводить всі збережені нотатки від юзера в порядку їх додавання.
    elif user_input == "earliest":
        print(notes_list)
        user_input = input("Please, enter your action: ")

    # Програма сортує та виводить всі збережені нотатки від юзера в зворотньому від додовання порядку.
    elif user_input == "latest":
        reversed_list = list(reversed(notes_list))
        print(reversed_list)
        user_input = input("Please, enter your action: ")

    # Програма сортує та виводить всі збережені нотатки від юзера від найдовшої до найкоротшої.
    elif user_input == "longest":
        longest_list = sorted(notes_list, key=len, reverse=True)
        print(longest_list)
        user_input = input("Please, enter your action: ")

    # Програма сортує та виводить всі збережені нотатки від юзера від найкоротшої до найдовшої.
    elif user_input == "shortest":
        shortest_list = sorted(notes_list, key=len)
        print(shortest_list)
        user_input = input("Please, enter your action: ")

    # При введенні некоретного ключового слова програма скаже юзеру ввести валідні дані.
    else:
        print("Enter valid action.")
        user_input = input("Please, enter your action: ")

#Вихід з програми по ключовому слову Exit (саме з великої букви як задано в умові).
print("You have finished")