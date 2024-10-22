# Define a simple nextDay procedure, that assumes every month has 30 days.

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """

    if day < 30:
        day += 1
    else:
        day = 1
        if month < 12:
            month += 1
        else:
            month = 1
            year += 1
    # YOUR CODE HERE
    return (year, month, day)
print(nextDay(2022, 5, 11))
print(nextDay(2022, 6, 30))
print(nextDay(2022, 12, 31))