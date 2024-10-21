"""Problem Statement
Consider the following problem:

Given a positive integer n, write a function, print_integers, that uses 4_recursion to print all numbers from n to 1.

For example, if n is 4, the function shuld print 4 3 2 1.

If we use iteration, the solution to the problem is simple. We can simply start at 4 and use a loop to print all numbers till 1. However, instead of using an interative approach, our goal is to solve this problem using 4_recursion."""
def print_integers(n):
    # TODO: Complete the function so that it uses 4_recursion to print all integers from n to 1
    sum = 0
    if n == 1:
        print(1)
        return
    print(n)
    print_integers(n - 1)
    # sum = int(n) + int(print_integers(n - 1))
    # print(sum)
    # return sum

print_integers(5)
"""Now let's consider what happens in the call stack when print_integers(5) is called.

As expected, a frame will be created for the print_integers() function and pushed onto the call stack.
Next, the parameter n gets the value 5.
Following this, the function starts executing. The base condition is checked. For n = 5, the base case is False, so we move forward and print the value of n.
In the next line, print_integers() is called again. This time it is called with the argument n - 1. The value of n in the current frame is 5. So this new function call takes place with value 4. Again, a new frame is created. Note that for every new call a new frame will be created. This frame is pushed onto the top of the stack.
Python now starts executing this frame. Again the base case is checked. It's False for n = 4. Following this, the n is printed and then print_integers() is called with argument n - 1 = 3.
The process keeps on like this until we hit the base case. When n <= 0, we return from the frame without calling the function print_integers() again. Because we have returned from the function call, the frame is discarded from the call stack and the next frame resumes execution right after the line where we left off."""
