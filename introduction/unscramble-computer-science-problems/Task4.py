"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    area_code_start = '('
    area_code_space = ' '
    telemarketer_nums = set()
    for call in calls:
        if area_code_start not in call[0] and area_code_space not in call[0]:
            telemarketer_nums.add(call[0])
        if area_code_start not in call[1] and area_code_space not in call[1]:
            telemarketer_nums.add(call[1])
    print("These numbers could be telemarketers:\n")
    telemarketer_nums = sorted(telemarketer_nums)
    for num in telemarketer_nums:
        print(num)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
