from sys import platform


def min_platforms(arrival, departure):
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    TODO - complete this method and return the minimum number of platforms (int) required
    so that no train has to wait for other(s) to leave
    """
    arrival = sorted(arrival)
    departure = sorted(departure)
    i = 0
    j = 0
    platform_current_required = 0
    platform_max = 0
    while (i <= len(arrival) - 1) and (j <= len(departure) - 1):
        if arrival[i] < departure[j]:
            platform_current_required += 1
            i += 1
            if (platform_current_required > platform_max):
                platform_max = platform_current_required
        else:
            platform_current_required -= 1
            j += 1
    return platform_max


def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]

    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]

test_function(test_case)

arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
test_case = [arrival, departure, 2]
test_function(test_case)
