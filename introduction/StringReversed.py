# Code

def string_reverser(our_string):
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """

    # TODO: Write your solution here
    # reversed_string = ""
    # str_length = len(our_string)
    # for i in range(0,str_length):
    #     reversed_string += our_string[str_length - i - 1: str_length-i]
    # return reversed_string
    # New empty string for us to build on
    new_string = ""

    # Iterate over old string
    for i in range(len(our_string)):
        # Grab the charecter from the back of the string and add them to the new string
        print(our_string[(len(our_string)-1)-i])
        new_string += our_string[(len(our_string)-1)-i]

    # Return our solution
    return new_string
print("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print(
        "Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
print("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")
