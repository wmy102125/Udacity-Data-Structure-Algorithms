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
    area_code = '(080)'
    area_code_mobile_prefix = set()
    # Part A: Find all of the area codes and mobile prefixes called by people in Bangalore
    fixed_line_number = set()
    fixed_call_count = 0
    fixed_receive_count = 0
    for row in calls:
        call_number = row[0]
        # if it is the Bangalore's call number
        if call_number.startswith(area_code):
            # the fixed line number
            fixed_call_count += 1
            receive_number = row[1]
            # the receive number's are code is 080
            if receive_number.startswith(area_code):
                fixed_receive_count += 1
            if receive_number.startswith("("):
                # fixed line number
                area_code_mobile_prefix.add(receive_number[0:receive_number.index(")") + 1])
            elif receive_number.startswith("140"):
                # Telemarketers' number
                area_code_mobile_prefix.add(140)
            else:
                # mobile number
                area_code_mobile_prefix.add(receive_number[0:4])

    area_code_mobile_prefix = sorted(area_code_mobile_prefix)

    print("The numbers called by people in Bangalore have codes:")
    area_code_mobile_prefix = sorted(area_code_mobile_prefix)
    for num in area_code_mobile_prefix:
        print(num)

    print("%.2f percent of calls from fixed lines in Bangalore are calls \
        to other fixed lines in Bangalore." % (fixed_receive_count * 100 / fixed_call_count))


    """
    TASK 3:
    (080) is the area code for fixed line telephones in Bangalore.
    Fixed line numbers include parentheses, so Bangalore numbers
    have the form (080)xxxxxxx.)
    
    Part A: Find all of the area codes and mobile prefixes called by people
    in Bangalore. In other words, the calls were initiated by "(080)" area code
    to the following area codes and mobile prefixes:
     - Fixed lines start with an area code enclosed in brackets. The area
       codes vary in length but always begin with 0.
     - Mobile numbers have no parentheses, but have a space in the middle
       of the number to help readability. The prefix of a mobile number
       is its first four digits, and they always start with 7, 8 or 9.
     - Telemarketers' numbers have no parentheses or space, but they start
       with the area code 140.
    
    Print the answer as part of a message:
    "The numbers called by people in Bangalore have codes:"
     <list of codes>
    The list of codes should be print out one per line in lexicographic order with no duplicates.
    
    Part B: What percentage of calls from fixed lines in Bangalore are made
    to fixed lines also in Bangalore? In other words, of all the calls made
    from a number starting with "(080)", what percentage of these calls
    were made to a number also starting with "(080)"?
    
    Print the answer as a part of a message::
    "<percentage> percent of calls from fixed lines in Bangalore are calls
    to other fixed lines in Bangalore."
    The percentage should have 2 decimal digits
    """
