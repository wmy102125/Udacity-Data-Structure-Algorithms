"""Problem Statement
Suppose there is a staircase that you can climb in either 1 step, 2 steps, or 3 steps. In how many possible ways can you climb the staircase if the staircase has n steps? Write a recursive function to solve the problem.

Example:

n == 1 then answer = 1

n == 3 then answer = 4
The output is 4 because there are four ways we can climb the staircase:

1 step + 1 step + 1 step
1 step + 2 steps
2 steps + 1 step
3 steps
n == 5 then answer = 13"""
"""
param: n - number of steps in the staircase
Return number of possible ways in which you can climb the staircase
"""


def staircase(n):
    '''Hint'''
    # Base Case - What holds true for minimum steps possible i.e., n == 0, 1, 2 or 3? Return the number of ways the child can climb n steps.

    # Recursive Step - Split the solution into base case if n > 3.
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)

    pass


print(staircase(1))
print(staircase(2))
print(staircase(3))
print(staircase(4))
print(staircase(5))
