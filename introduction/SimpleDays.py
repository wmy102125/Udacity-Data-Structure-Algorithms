def isLeapYear(year):
    ## Leap Year alogorithm
    # if year modulo 400 is 0 then
    #     is_leap_year
    # else if year modulo 100 is 0 then
    #     not_leap_year
    # else if year modulo 4 is 0 then
    #     is_leap_year
    # else
    #     not_leap_year
    if year % 400 ==0:
        return True
    elif year % 100 == 0 :
        return True
    elif year % 4 == 0 :
        return True
    else :
        return False
def daysInMonth(year,month):
    if month == 1 or month ==3 or month ==5 or month ==7 or month ==8 or month ==10 or month ==12:
        return 31
    elif month ==2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
        return 30
def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year,month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    assert not date_is_before(year2, month2, day2,year1, month1, day1)
    days = 0
    while (True):
        if date_is_before(year1, month1, day1, year2, month2, day2):
            year1, month1, day1 = nextDay(year1, month1, day1)
            days += 1
        else:
            break
    # YOUR CODE HERE!
    return days


def date_is_before(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            if day1 < day2:
                return True
    return False


# Testing code -- do not change
def codeTest(year1, month1, day1, year2, month2, day2, answer):
    try:
        result = daysBetweenDates(year1, month1, day1, year2, month2, day2)
        if result == answer and answer != "AssertionError":
            return "correct"
        else:
            return "incorrect", answer

    except AssertionError:
        if answer == "AssertionError":
            return "correct AssertionError"
        else:
            return "incorrect AssertionError"


#print(daysBetweenDates(2012, 9, 30, 2011, 10, 30))


##print(codeTest(2012,9,30,2012,10,30, 30))
##print(codeTest(2012,9,30,2012,10,30, 12))
##print(codeTest(2013,1,1,1999,12,31, "AssertionError"))
def test():
    assert daysBetweenDates(2012, 9, 30, 2012, 10, 30) == 30
    assert daysBetweenDates(2012, 9, 30, 2012, 10, 1) == 1
    assert daysBetweenDates(2012, 1, 1, 2013, 1, 1) == 366
    assert daysBetweenDates(2011, 1, 1, 2012, 1, 1) == 365
    assert nextDay(2013, 1, 1) == (2013, 1, 2)
    print("Tests finnished!")
test()