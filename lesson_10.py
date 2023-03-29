import re

# Task 1
def make_rows(file):
    with open(file, "r+") as file:
        lines = file.read()
        new_list = re.sub(r'\.', '', lines)
        print(new_list)
        return new_list


make_rows("domains.txt")


# Task 2
def print_surname(file):
    with open(file, "r+") as file:
        lines = file.read().split('\n')
        for line in lines:
            split_row = re.sub(r',', '', line)
            final_row = split_row.split(' ')
            print(final_row[1])


print_surname("names.txt")


#Task 3
def find_date_in_row(file):
    with open(file, "r+") as f:
        row = f.read().split('\n')
        pattern = r'^(?:\d{1,2}(?:st|nd|rd|th)\s)?(?:January|February|March|April|May|June|July|August|September|October' \
                  r'|November|December)\s\d{4}'
        dates_row = []
        for el in row:
            match = re.match(pattern, el)
            if match:
                dates_row.append({"date": match.group()})
        print(dates_row)
        return dates_row


find_date_in_row("authors.txt")
