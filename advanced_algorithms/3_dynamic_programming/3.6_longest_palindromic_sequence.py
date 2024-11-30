def lps(input_string):
    # TODO: Complete this implementation of the LPS function
    # The function should return one value: the LPS length for the given input string
    loop_table = [[0 for x in range(len(input_string))] for x in range(len(input_string))]
    for i in range(len(input_string)):
        loop_table[i][i] = 1
    for index_row in reversed(range(len(input_string))):
        for index_column in range(index_row + 1, len(input_string)):
            if input_string[index_column] == input_string[index_row]:
                loop_table[index_row][index_column] = loop_table[index_row + 1][index_column] + 2
            else:
                loop_table[index_row][index_column] = max(loop_table[index_row][index_column - 1],
                                                          loop_table[index_row + 1][index_column])
    return loop_table[0][len(input_string)-1]

#solution
## Solution

# imports for printing a matrix, nicely
import pprint

pp = pprint.PrettyPrinter()


# complete LPS solution
def lps_solution(input_string):
    n = len(input_string)

    # create a lookup table to store results of subproblems
    L = [[0 for x in range(n)] for x in range(n)]

    # strings of length 1 have LPS length = 1
    for i in range(n):
        L[i][i] = 1

        # consider all substrings
    for s_size in range(2, n + 1):
        for start_idx in range(n - s_size + 1):
            end_idx = start_idx + s_size - 1
            if s_size == 2 and input_string[start_idx] == input_string[end_idx]:
                # match with a substring of length 2
                L[start_idx][end_idx] = 2
            elif input_string[start_idx] == input_string[end_idx]:
                # general match case
                L[start_idx][end_idx] = L[start_idx + 1][end_idx - 1] + 2
            else:
                # no match case, taking the max of two values
                L[start_idx][end_idx] = max(L[start_idx][end_idx - 1], L[start_idx + 1][end_idx]);

                # debug line
    # pp.pprint(L)

    return L[0][n - 1]  # value in top right corner of matrix
def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


string = 'BxAoNxAoNxA'
solution = 5
test_case = [string, solution]
test_function(test_case)

string = 'BANANO'
solution = 3
test_case = [string, solution]
test_function(test_case)

string = "TACOCAT"
solution = 7
test_case = [string, solution]
test_function(test_case)
