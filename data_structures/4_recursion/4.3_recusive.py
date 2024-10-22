class Recurtion:
    def recursive(input):
        if input == 0:
            return input
        else:
            output = Recurtion.recursive(input - 1)
        return output


print(Recurtion.recursive(10000))


# Implement sum_integers(n) to calculate the sum of all integers from  1
#  to  𝑛
#  using 4_recursion. For example, sum_integers(3) should return  6
# ( 1+2+3
# ).
def sum_integers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_integers(n - 1)
    pass

print(sum_integers(3))