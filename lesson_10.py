json_string = [
    {
        "name": "Ivan",
        "age": 40
    },
    {
        "name": "Olena",
        "age": 50
    },
    {
        "name": "Maryna",
        "age": 32
    }
]

import json

with open("test_file.json", "w") as writer:
    json.dump(json_string, writer, indent=4)
with open("test_file.json", "r") as reader:
    data = json.load(reader)
    for el in data:
        print(el["name"])



