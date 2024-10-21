"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    longest_time = 0
    call_number = None
    call_date = ""
    for call in calls:
        curation = float(call[3])
        if longest_time < curation:
            longest_time = curation
            call_number = call[0]
            call_date = call[2]

    print("%s spent the longest time, %s seconds, on the phone during "
        "%s" % (call_number, longest_time,call_date))


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

