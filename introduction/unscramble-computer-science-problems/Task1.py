"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


def count_phone_numbers():
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)
        number_sets = set()
        for row in texts:
            number_sets.add(row[0])
            number_sets.add(row[1])

    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
        call_sets = set()
        for row in calls:
            call_sets.add(row[0])
            call_sets.add(row[1])
    call_text_num = number_sets | call_sets
    print("There are %s different telephone numbers in the records." % len(call_text_num))
count_phone_numbers()


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
