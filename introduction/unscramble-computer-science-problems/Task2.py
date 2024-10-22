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
    phone_dict = dict()
    for call in calls:
        if call[0] in phone_dict:
            phone_dict[call[0]] +=  int(call[3])
        else:
            phone_dict[call[0]] = int(call[3])
        if call[1] in phone_dict:
            phone_dict[call[1]] += int(call[3])
        else:
            phone_dict[call[1]] = int(call[3])
    max_duration_phone = max(phone_dict,key=phone_dict.get)
    max_duration = max(phone_dict.values())
    print("%s spent the longest time, %s seconds, on the phone during September 2016" % (max_duration_phone, max_duration))




"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

