from operator import is_not
from xmlrpc.client import Boolean


def prod(a,b):
    # TODO change output to the product of a and b
    output = a*b;
    return output

def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        # TODO: update i and n
        # Hint: i is a successive integer and n is the previous product
        n = output;
        i+=1;


# Test cases
my_gen = fact_gen()
num = 5
# for i in range(num):
#     print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120

# Define a function check_sudoku() here:
def check_sudoku(square):
    return check_item(square) and check_item(columSquare(square))

def check_item(square):
    correct = True
    sourceList = square[0]
    for rowItem in square:
        for source in sourceList:
            if rowItem.count(source) != 1 or bool(isinstance(source,int)-1) :
                correct = False
                break
    return correct


def columSquare(square):
    ## column_list =[[None for i in range(len(square[0]))]for j in range(len(square))]
    column_list = [[] for j in range(len(square))]
    x = 0
    for row in square:
        y = 0;
        for column in row:
            column_list[y].insert(x,column);
            y += 1
        x += 1
    return column_list;


# Test cases
correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]
incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]
incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]
incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]
incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]
incorrect5 = [[1, 1.5],
              [1.5, 1]]

print(check_sudoku(incorrect))
# >>> False
print(check_sudoku(correct))
# >>> True
print(check_sudoku(incorrect2))
# >>> False
print(check_sudoku(incorrect3))
# >>> False
print(check_sudoku(incorrect4))
# >>> False
print(check_sudoku(incorrect5))
# >>> False