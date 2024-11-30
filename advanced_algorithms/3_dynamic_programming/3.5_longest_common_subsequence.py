def lcs(string_a, string_b):
    loop_table = [[0 for x in range(len(string_b) + 1)] for i in range(len(string_a) + 1)]
    for index_a, char_a in enumerate(string_a):
        for index_b, char_b in enumerate(string_b):
            if char_b == char_a:
                # match : diagonal addition 1
                loop_table[index_a + 1][index_b + 1] = loop_table[index_a][index_b] + 1
            else:
                # no match:max(left,top)
                loop_table[index_a + 1][index_b + 1] = max(loop_table[index_a][index_b + 1],
                                                           loop_table[index_a + 1][index_b])
    return loop_table[-1][-1]


# solution
def lcs_solution(string_a, string_b):
    # initialize the matrix
    lookup_table = [[0 for x in range(len(string_b) + 1)] for x in range(len(string_a) + 1)]

    # enumerate(str) returns a tuple containing the index and character in each iteration
    for char_a_i, char_a in enumerate(string_a):

        for char_b_i, char_b in enumerate(string_b):

            # If there is a match,
            # fill that grid cell with the value to the top-left of that cell plus one
            if char_a == char_b:
                lookup_table[char_a_i + 1][char_b_i + 1] = lookup_table[char_a_i][char_b_i] + 1

            # If there is not a match,
            # take the maximum value from either directly to the left or the top cell
            else:
                lookup_table[char_a_i + 1][char_b_i + 1] = max(
                    lookup_table[char_a_i][char_b_i + 1],
                    lookup_table[char_a_i + 1][char_b_i])

    # the bottom-right cell will hold the non-normalized LCS length value.
    return lookup_table[-1][-1]


## Test cell

# Run this cell to see how your function is working
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

lcs_val1 = lcs(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

lcs_val2 = lcs(test_A2, test_B2)

print('LCS val 1 = ', lcs_val1)
assert lcs_val1 == 5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2==7, "Incorrect LCS value."
print('Tests passed!')
