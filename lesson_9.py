import re


#Task 1
pattern = r'^[a-zA-Z0-9_]*$'
string = input("Enter your string:")

if re.search(pattern, string):
    print("Valid string")
else:
    print("Invalid string")


#Task 2
string = ["example (.com)", "github (.com)", "stackoverflow (.com)"]
pattern = r'\(.com\)'
for el in string:
    string = re.sub(pattern, '', el)
    print(string)

#Task 3
string = "HelloMyNameIsOlena"
pattern = r'(?<!^)(?=[A-Z])'
new_string = re.sub(pattern, ' ', string)

print(new_string)