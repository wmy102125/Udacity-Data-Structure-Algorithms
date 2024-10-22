"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


def find_telemarketer_num():
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)
        no_phone_set = set()
        for text in texts:
            no_phone_set.add(text[0])
            no_phone_set.add(text[1])
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
        outgoing_set = set()
        for call in calls:
            outgoing_set.add(call[0])
            no_phone_set.add(call[1])
        telemarketer_num = outgoing_set.difference(no_phone_set)
        for i in telemarketer_num:
            print(i)
find_telemarketer_num()


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
